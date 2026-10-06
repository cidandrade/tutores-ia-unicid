# Como instalar o tutor no Claude

No Claude, o tutor é uma **habilidade** (skill): você envia um arquivo `.zip` uma vez e ela passa a funcionar em todas as suas conversas. Leva uns 5 minutos.

## 1. Baixe o arquivo da sua disciplina

Baixe o `.zip` da sua disciplina na [tabela do README](../README.md#disciplinas). **Não descompacte**: o Claude recebe o `.zip` inteiro.

## 2. Libere a leitura do material

O tutor lê o índice e o material da disciplina pela internet. Para isso:

1. Entre em [claude.ai](https://claude.ai) com a sua conta.
2. Clique no seu nome (canto inferior esquerdo) → **Configurações** → **Recursos**.
3. Ative **Execução de código na nuvem e criação de arquivos**.
4. Ative **Permitir acesso de rede externo**. Em **Lista de domínios permitidos**, garanta que estes endereços estejam liberados (ou escolha a opção que libera todos os domínios):
   - `raw.githubusercontent.com`
   - `drive.google.com`
   - `docs.google.com`

## 3. Envie a habilidade

1. No menu da esquerda, clique em **Personalização**.
2. Abra a aba **Habilidades**.
3. Clique em **+ Adicionar** → **Fazer upload de habilidade** e escolha o `.zip` que você baixou.
4. Em **Meus**, confira se a habilidade aparece (ex.: `tutor-mbd`) e se está **ativada**.

## 4. Use

Abra uma **conversa nova** e escreva normalmente sobre a disciplina. O Claude ativa o tutor sozinho quando percebe que o assunto é dela. Exemplos:

- "Não entendi o que é cardinalidade no DER."
- "Gere um simulado da A1."
- "Tirei 2,5 na A2. Quanto preciso na A1 para passar?"

Se ele não ativar o tutor, comece a mensagem com o nome da disciplina: "Na disciplina de Modelagem de Banco de Dados, ...".

## Se a sua conta não tiver Habilidades

Use um **Projeto**:

1. Baixe o arquivo de instruções da disciplina (`tutor-<sigla>-instrucoes.md`) na [tabela do README](../README.md#disciplinas).
2. No menu da esquerda, clique em **Projetos** → **Novo projeto** e dê o nome da disciplina.
3. Nas **instruções do projeto**, cole todo o conteúdo do arquivo de instruções e salve.
4. Converse com o tutor sempre **dentro desse projeto**.

## Problemas comuns

| O que acontece | O que fazer |
|---|---|
| O tutor diz que não consegue abrir o índice ou o material | Confira o passo 2 (execução de código, acesso de rede e domínios liberados). Se continuar, anexe à conversa o arquivo que ele pedir (você o encontra na pasta da disciplina no Drive). |
| O tutor responde, mas não cita o material | Peça: "Consulte o material da disciplina e cite o documento e a seção." |
| Ele resolve o trabalho por você | Não deveria. Avise o professor, com o print da conversa. |

## Atualizações

O tutor lê o material novo pela internet, então **você não precisa reinstalar** quando o professor publica uma aula. Reinstale só quando o professor avisar que saiu uma nova versão: baixe o `.zip` de novo, apague a habilidade antiga em **Personalização → Habilidades** e envie a nova.
