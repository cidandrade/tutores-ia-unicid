#!/usr/bin/env python3
"""Gera o índice do material de uma disciplina a partir da pasta pública do Drive.

Lista a pasta (recursivamente) pela Drive API v3 com uma API key, sem OAuth,
e atualiza indices/<sigla>.yaml (fonte estruturada, chave = ID do arquivo) e
indices/<sigla>.md (o que as skills leem pela URL raw).

Campos preenchidos pelo script: nome, tipo, caminho, modificado, links, status.
Campos manuais, preservados entre execuções: semana, resumo, topicos, secoes.
Arquivo novo ou com modifiedTime alterado fica com status "pendente" até o
/atualizar-indice preencher os campos manuais.

Uso:
    python scripts/gerar_indice.py <sigla> [--baixar-pendentes]
    python scripts/gerar_indice.py --todas [--baixar-pendentes]

A chave vem de GOOGLE_API_KEY (variável de ambiente ou .env na raiz).
"""
import argparse
import datetime
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISCIPLINAS = os.path.join(RAIZ, 'disciplinas')
INDICES = os.path.join(RAIZ, 'indices')
CACHE = os.path.join(RAIZ, '.cache')
API = 'https://www.googleapis.com/drive/v3'

PASTA = 'application/vnd.google-apps.folder'
GOOGLE = {
    # mimeType: (tipo, link de leitura, mimeType de exportação, extensão no cache)
    'application/vnd.google-apps.document': (
        'Google Docs',
        'https://docs.google.com/document/d/{id}/export?format=txt',
        'text/plain', '.txt'),
    'application/vnd.google-apps.presentation': (
        'Google Slides',
        'https://docs.google.com/presentation/d/{id}/export/txt',
        'text/plain', '.txt'),
    'application/vnd.google-apps.spreadsheet': (
        'Google Sheets',
        'https://docs.google.com/spreadsheets/d/{id}/export?format=csv',
        'text/csv', '.csv'),
}
DOWNLOAD = 'https://drive.google.com/uc?export=download&id={id}'
VISUALIZAR = 'https://drive.google.com/file/d/{id}/view'
CAMPOS_MANUAIS = ('semana', 'resumo', 'topicos', 'secoes')


def chave_api():
    chave = os.environ.get('GOOGLE_API_KEY')
    env = os.path.join(RAIZ, '.env')
    if not chave and os.path.exists(env):
        for linha in open(env, encoding='utf-8'):
            nome, _, valor = linha.strip().partition('=')
            if nome == 'GOOGLE_API_KEY':
                chave = valor.strip().strip('"\'')
    if not chave:
        sys.exit('GOOGLE_API_KEY não encontrada (variável de ambiente ou .env).')
    return chave


def pedir(caminho, params, chave, bruto=False):
    url = f'{API}/{caminho}?' + urllib.parse.urlencode({**params, 'key': chave})
    try:
        with urllib.request.urlopen(url) as resp:
            return resp.read() if bruto else json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            msg = json.load(e)['error']['message']
        except Exception:
            msg = e.reason
        sys.exit(f'Erro {e.code} na Drive API ({caminho}): {msg}')


def listar(pasta, chave, caminho=''):
    """Todos os arquivos (não pastas) abaixo de `pasta`, com o caminho relativo."""
    arquivos, pagina = [], None
    while True:
        params = {
            'q': f"'{pasta}' in parents and trashed=false",
            'fields': 'nextPageToken,files(id,name,mimeType,modifiedTime)',
            'pageSize': 1000,
        }
        if pagina:
            params['pageToken'] = pagina
        resp = pedir('files', params, chave)
        for f in resp.get('files', []):
            if f['mimeType'] == PASTA:
                arquivos += listar(f['id'], chave, f"{caminho}{f['name']}/")
            else:
                f['caminho'] = caminho
                arquivos.append(f)
        pagina = resp.get('nextPageToken')
        if not pagina:
            return arquivos


def tipo_e_link(f):
    if f['mimeType'] in GOOGLE:
        tipo, link, _, _ = GOOGLE[f['mimeType']]
        return tipo, link.format(id=f['id'])
    ext = os.path.splitext(f['name'])[1].lstrip('.').upper()
    tipo = {'MD': 'Markdown'}.get(ext, ext or f['mimeType'])
    return tipo, DOWNLOAD.format(id=f['id'])


def atualizar(cfg, chave):
    """Mescla a listagem do Drive no YAML. Devolve (dados, relatório)."""
    sigla = cfg['sigla']
    arq_yaml = os.path.join(INDICES, f'{sigla}.yaml')
    antigos = {}
    if os.path.exists(arq_yaml):
        antigos = (yaml.safe_load(open(arq_yaml, encoding='utf-8')) or {}).get('arquivos') or {}

    novos, alterados, arquivos = [], [], {}
    for f in listar(cfg['pasta_drive'], chave):
        tipo, leitura = tipo_e_link(f)
        anterior = antigos.get(f['id'], {})
        item = {
            'nome': f['name'],
            'tipo': tipo,
            'caminho': f['caminho'],
            'modificado': f['modifiedTime'],
            'link_leitura': leitura,
            'link_visualizacao': VISUALIZAR.format(id=f['id']),
            'status': anterior.get('status', 'pendente'),
        }
        for campo in CAMPOS_MANUAIS:
            item[campo] = anterior.get(campo, [] if campo in ('topicos', 'secoes') else '')
        if not anterior:
            novos.append(f['name'])
        elif anterior.get('modificado') != f['modifiedTime']:
            item['status'] = 'pendente'
            alterados.append(f['name'])
        arquivos[f['id']] = item

    removidos = [a['nome'] for i, a in antigos.items() if i not in arquivos]
    dados = {
        'disciplina': cfg['disciplina'],
        'sigla': sigla,
        'pasta_drive': cfg['pasta_drive'],
        'atualizado_em': datetime.date.today().isoformat(),
        'arquivos': dict(sorted(arquivos.items(), key=lambda kv: ordem(kv[1]))),
    }
    return dados, {'novos': novos, 'alterados': alterados, 'removidos': removidos}


def ordem(item):
    """Por semana (numérica primeiro, depois texto, depois sem semana) e nome."""
    s = str(item.get('semana') or '').strip()
    grupo = (0, int(s), '') if s.isdigit() else (1, 0, s) if s else (2, 0, '')
    return grupo + (item['caminho'] + item['nome'],)


def titulo(item):
    return item['caminho'] + item['nome']


def renderizar(dados):
    linhas = [
        f"# Índice do material: {dados['disciplina']}",
        '',
        f"> Atualizado em {dados['atualizado_em']}. Material oficial da disciplina, "
        'numa pasta pública do Google Drive. Para ler um arquivo, use o '
        '**link de leitura** (abre sem login). O link de visualização é para o aluno.',
    ]
    grupo_atual = None
    for item in dados['arquivos'].values():
        s = str(item.get('semana') or '').strip()
        grupo = (f'Semana {s}' if s.isdigit() else s) if s else 'Sem semana definida'
        if grupo != grupo_atual:
            linhas += ['', f'## {grupo}']
            grupo_atual = grupo
        linhas += ['', f'### {titulo(item)}', '']
        linhas.append(f"- **Tipo:** {item['tipo']} · **Modificado:** {item['modificado'][:10]}")
        if item['status'] == 'pendente' and not item.get('resumo'):
            linhas.append('- **Resumo:** _pendente_')
        else:
            if item.get('resumo'):
                linhas.append(f"- **Resumo:** {' '.join(str(item['resumo']).split())}")
            if item.get('topicos'):
                linhas.append(f"- **Tópicos:** {'; '.join(item['topicos'])}")
            if item.get('secoes'):
                linhas.append(f"- **Seções:** {'; '.join(item['secoes'])}")
        linhas.append(f"- **Leitura:** {item['link_leitura']}")
        linhas.append(f"- **Visualizar:** {item['link_visualizacao']}")
    return '\n'.join(linhas) + '\n'


def baixar_pendentes(dados, chave):
    """Baixa os pendentes para .cache/<sigla>/, para o /atualizar-indice ler."""
    destino = os.path.join(CACHE, dados['sigla'])
    os.makedirs(destino, exist_ok=True)
    caminhos = []
    for id_, item in dados['arquivos'].items():
        if item['status'] != 'pendente':
            continue
        mime = next((m for m, g in GOOGLE.items() if g[0] == item['tipo']), None)
        if mime:
            _, _, exportar, ext = GOOGLE[mime]
            conteudo = pedir(f'files/{id_}/export', {'mimeType': exportar}, chave, bruto=True)
            nome = os.path.splitext(item['nome'])[0] + ext
        else:
            conteudo = pedir(f'files/{id_}', {'alt': 'media'}, chave, bruto=True)
            nome = item['nome']
        arq = os.path.join(destino, f"{id_}__{re.sub(r'[/\\]', '_', nome)}")
        with open(arq, 'wb') as fh:
            fh.write(conteudo)
        caminhos.append(os.path.relpath(arq, RAIZ))
    return caminhos


def processar(sigla, chave, baixar):
    arq_cfg = os.path.join(DISCIPLINAS, sigla, 'config.yaml')
    if not os.path.exists(arq_cfg):
        sys.exit(f'Disciplina desconhecida: {sigla} (falta {os.path.relpath(arq_cfg, RAIZ)})')
    cfg = yaml.safe_load(open(arq_cfg, encoding='utf-8'))
    dados, rel = atualizar(cfg, chave)

    os.makedirs(INDICES, exist_ok=True)
    with open(os.path.join(INDICES, f'{sigla}.yaml'), 'w', encoding='utf-8') as fh:
        yaml.safe_dump(dados, fh, allow_unicode=True, sort_keys=False, width=1000)
    with open(os.path.join(INDICES, f'{sigla}.md'), 'w', encoding='utf-8') as fh:
        fh.write(renderizar(dados))

    pendentes = sum(a['status'] == 'pendente' for a in dados['arquivos'].values())
    print(f"[{sigla}] {len(dados['arquivos'])} arquivos · {len(rel['novos'])} novos · "
          f"{len(rel['alterados'])} alterados · {len(rel['removidos'])} removidos · "
          f"{pendentes} pendentes")
    for nome in rel['alterados']:
        print(f'  alterado: {nome}')
    for nome in rel['removidos']:
        print(f'  removido do Drive (saiu do índice): {nome}')
    if baixar:
        for caminho in baixar_pendentes(dados, chave):
            print(f'  baixado: {caminho}')


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument('sigla', nargs='?', help='sigla da disciplina (ex.: dp)')
    p.add_argument('--todas', action='store_true', help='todas as disciplinas')
    p.add_argument('--baixar-pendentes', action='store_true',
                   help='baixa os arquivos pendentes para .cache/<sigla>/')
    args = p.parse_args()
    if bool(args.sigla) == args.todas:
        p.error('informe uma sigla ou --todas')

    siglas = sorted(os.listdir(DISCIPLINAS)) if args.todas else [args.sigla]
    chave = chave_api()
    for sigla in siglas:
        if os.path.exists(os.path.join(DISCIPLINAS, sigla, 'config.yaml')):
            processar(sigla, chave, args.baixar_pendentes)


if __name__ == '__main__':
    main()
