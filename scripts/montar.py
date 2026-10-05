#!/usr/bin/env python3
"""Monta as skills de tutoria a partir do modelo do núcleo e das disciplinas.

Para cada disciplinas/<sigla>/, substitui os marcadores de _modelo/ e grava:
- skills/<nome_skill>/            SKILL.md + references/ (versionado)
- dist/<nome_skill>.zip           pronto para upload no Claude
- dist/<nome_skill>-instrucoes.md texto único para GPT e Gem (até 8.000 caracteres)

Trechos de ementa.md e avaliacao-a2.md entre <!-- só-skill --> e <!-- /só-skill -->
entram só na skill; ficam fora das instruções portáteis, para caber no limite.

Uso:
    python scripts/montar.py <sigla>
    python scripts/montar.py --todas
"""
import argparse
import os
import re
import shutil
import sys
import zipfile

import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELO = os.path.join(RAIZ, '_modelo')
DISCIPLINAS = os.path.join(RAIZ, 'disciplinas')
SKILLS = os.path.join(RAIZ, 'skills')
DIST = os.path.join(RAIZ, 'dist')
URL_INDICE = 'https://raw.githubusercontent.com/cidandrade/tutores-ia-unicid/main/indices/{sigla}.md'

CAMPOS = ('disciplina', 'nome_skill', 'especialidade', 'gatilhos')
# Ordem das referências: a mesma da tabela do SKILL.md e das instruções portáteis.
# (arquivo final, origem, vem da disciplina?)
REFERENCIAS = (
    ('consulta-material.md', 'consulta-material.md.tmpl', False),
    ('ementa.md', 'ementa.md', True),
    ('avaliacao-a2.md', 'avaliacao-a2.md', True),
    ('avaliacao.md', 'avaliacao.md', False),
    ('simulados.md', 'simulados.md', False),
)
LIMITE_INSTRUCOES = 8000
LIMITE_DESCRIPTION = 1024
NOME_VALIDO = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
SO_SKILL = re.compile(r'<!-- só-skill -->(.*?)<!-- /só-skill -->', re.S)
DATA_ZIP = (2026, 1, 1, 0, 0, 0)  # data fixa: o mesmo conteúdo gera o mesmo zip


class Erro(Exception):
    pass


def ler(caminho):
    with open(caminho, encoding='utf-8') as f:
        return f.read()


def gravar(caminho, texto):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(texto)


def carregar(sigla):
    """Lê config e arquivos da disciplina; junta todos os problemas numa mensagem só."""
    pasta = os.path.join(DISCIPLINAS, sigla)
    arq_cfg = os.path.join(pasta, 'config.yaml')
    if not os.path.isfile(arq_cfg):
        raise Erro(f'disciplina desconhecida (falta {os.path.relpath(arq_cfg, RAIZ)})')
    cfg = yaml.safe_load(ler(arq_cfg)) or {}
    problemas = [f'config.yaml: "{c}" vazio' for c in CAMPOS if not str(cfg.get(c) or '').strip()]
    arquivos = {}
    for final, origem, da_disciplina in REFERENCIAS:
        if not da_disciplina:
            continue
        caminho = os.path.join(pasta, origem)
        if not os.path.isfile(caminho):
            problemas.append(f'falta {os.path.relpath(caminho, RAIZ)}')
            continue
        texto = ler(caminho)
        if texto.count('<!-- só-skill -->') != texto.count('<!-- /só-skill -->'):
            problemas.append(f'{origem}: marcadores só-skill desbalanceados')
        if not re.match(r'\s*# ', texto):
            problemas.append(f'{origem}: precisa começar com um título "# ..."')
        arquivos[final] = texto
    if problemas:
        raise Erro('\n'.join('  - ' + p for p in problemas))
    return cfg, arquivos


def substituir(texto, valores):
    for chave, valor in valores.items():
        texto = texto.replace('{{' + chave + '}}', valor)
    return texto


def validar(skill_md, textos):
    m = re.match(r'---\n(.*?)\n---\n', skill_md, re.S)
    if not m:
        raise Erro('SKILL.md sem frontmatter')
    meta = yaml.safe_load(m.group(1))
    nome, desc = str(meta.get('name', '')), str(meta.get('description', ''))
    problemas = []
    if not NOME_VALIDO.match(nome) or len(nome) > 64:
        problemas.append(f'name "{nome}": use só minúsculas, números e hífens (até 64)')
    if 'claude' in nome or 'anthropic' in nome:
        problemas.append(f'name "{nome}": não pode conter "claude" nem "anthropic"')
    if len(desc) > LIMITE_DESCRIPTION:
        problemas.append(f'description com {len(desc)} caracteres (máximo {LIMITE_DESCRIPTION})')
    for arquivo, texto in textos.items():
        sobra = sorted(set(re.findall(r'\{\{\w+\}\}', texto)))
        if sobra:
            problemas.append(f'{arquivo}: marcadores sem valor {", ".join(sobra)}')
    if problemas:
        raise Erro('\n'.join('  - ' + p for p in problemas))


def titulo(texto):
    return re.match(r'\s*# (.+)', texto).group(1).strip()


def portatil(skill_md, refs):
    """Junta SKILL.md e referências num texto único, sem frontmatter nem caminhos de arquivo."""
    corpo = re.sub(r'^---\n.*?\n---\n+', '', skill_md, flags=re.S)
    corpo = re.split(r'\n## Referências\n', corpo)[0].rstrip()
    titulos = {final: titulo(texto) for final, texto in refs.items()}
    partes = {'núcleo': corpo}
    for final, texto in refs.items():
        texto = SO_SKILL.sub('', texto)
        texto = re.sub(r'^(#+) ', r'#\1 ', texto, flags=re.M)  # um nível abaixo do título do tutor
        texto = re.sub(r'\n{3,}', '\n\n', texto).strip()
        partes[final] = texto
    texto = '\n\n'.join(partes.values()) + '\n'

    def secao(m):
        nome = titulos.get(m.group(2))
        if nome is None:
            raise Erro(f'referência desconhecida: references/{m.group(2)}')
        return f'{"na " if m.group(1) else ""}seção "{nome}"'

    texto = re.sub(r'(em )?`references/([\w.-]+)`', secao, texto)
    return texto, partes


def zipar(pasta, destino):
    nome = os.path.basename(pasta)
    with zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED) as z:
        for atual, dirs, arquivos in os.walk(pasta):
            dirs.sort()
            for arq in sorted(arquivos):
                caminho = os.path.join(atual, arq)
                info = zipfile.ZipInfo(os.path.join(nome, os.path.relpath(caminho, pasta)), DATA_ZIP)
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, ler(caminho))


def montar(sigla):
    cfg, arquivos_disc = carregar(sigla)
    nome = cfg['nome_skill']
    valores = {
        'DISCIPLINA': cfg['disciplina'],
        'SIGLA': sigla,
        'NOME_SKILL': nome,
        'ESPECIALIDADE': str(cfg['especialidade']).strip(),
        'GATILHOS': str(cfg['gatilhos']).strip(),
        'URL_INDICE': URL_INDICE.format(sigla=sigla),
    }
    skill_md = substituir(ler(os.path.join(MODELO, 'SKILL.md.tmpl')), valores)
    refs = {}
    for final, origem, da_disciplina in REFERENCIAS:
        if da_disciplina:
            refs[final] = substituir(arquivos_disc[final], valores)
        else:
            refs[final] = substituir(ler(os.path.join(MODELO, 'references', origem)), valores)
    validar(skill_md, {'SKILL.md': skill_md, **refs})

    instrucoes, partes = portatil(skill_md, refs)
    if len(instrucoes) > LIMITE_INSTRUCOES:
        detalhe = '\n'.join(f'    {p}: {len(t)}' for p, t in partes.items())
        raise Erro(f'  - instruções portáteis com {len(instrucoes)} caracteres '
                   f'(máximo {LIMITE_INSTRUCOES}). Por parte:\n{detalhe}\n'
                   '    Marque trechos de ementa.md ou avaliacao-a2.md com <!-- só-skill -->.')

    pasta = os.path.join(SKILLS, nome)
    shutil.rmtree(pasta, ignore_errors=True)
    gravar(os.path.join(pasta, 'SKILL.md'), skill_md)
    for final, texto in refs.items():
        texto = re.sub(r'<!-- /?só-skill -->\n?', '', texto)
        gravar(os.path.join(pasta, 'references', final), texto)

    os.makedirs(DIST, exist_ok=True)
    zipar(pasta, os.path.join(DIST, nome + '.zip'))
    gravar(os.path.join(DIST, nome + '-instrucoes.md'), instrucoes)
    return nome, len(instrucoes)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('sigla', nargs='?', help='sigla da disciplina (ex.: dp)')
    g.add_argument('--todas', action='store_true', help='monta todas as disciplinas')
    args = p.parse_args()
    if args.todas:
        siglas = sorted(d for d in os.listdir(DISCIPLINAS)
                        if os.path.isfile(os.path.join(DISCIPLINAS, d, 'config.yaml')))
    else:
        siglas = [args.sigla]
    falhas = 0
    for sigla in siglas:
        try:
            nome, tamanho = montar(sigla)
            print(f'{sigla}: skills/{nome}/, dist/{nome}.zip, '
                  f'instruções com {tamanho}/{LIMITE_INSTRUCOES} caracteres')
        except Erro as e:
            falhas += 1
            print(f'{sigla}: não montada\n{e}', file=sys.stderr)
    if falhas:
        sys.exit(1)


if __name__ == '__main__':
    main()
