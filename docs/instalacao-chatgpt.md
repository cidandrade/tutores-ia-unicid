# Como instalar o tutor no ChatGPT

O ChatGPT aceita o mesmo pacote do Claude: o tutor é uma **skill** no formato aberto Agent Skills. Se a sua conta ainda não tiver skills, dá para criar um **GPT personalizado** com as instruções. Leva uns 5 minutos.

## Opção 1 — Skill (recomendada)

1. Baixe o `.zip` da sua disciplina na [tabela do README](../README.md#disciplinas). **Não descompacte.**
2. Entre em [chatgpt.com](https://chatgpt.com) e abra uma conversa nova.
3. Anexe o `.zip` (botão **+** da caixa de mensagem) e escreva: **"Instale esta skill."**
4. Confirme a instalação quando o ChatGPT pedir. A partir daí, o tutor fica disponível nas suas conversas.

> Skills ainda estão em fase beta e chegando aos poucos aos planos. Se o ChatGPT disser que não consegue instalar, use a Opção 2.

## Opção 2 — GPT personalizado

1. Baixe o arquivo `tutor-<sigla>-instrucoes.md` da sua disciplina na [tabela do README](../README.md#disciplinas) e abra-o num editor de texto.
2. Em [chatgpt.com](https://chatgpt.com), clique em **GPTs** → **Criar** (ou acesse [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor)) e abra a aba **Configurar**.
3. Preencha:
   - **Nome:** o nome da disciplina, por exemplo "Tutor de Modelagem de Banco de Dados".
   - **Instruções:** cole **todo** o conteúdo do arquivo de instruções, sem cortar nada.
4. Em **Recursos**, deixe **Pesquisa na Web** ligada. É assim que o tutor lê o índice e o material da disciplina.
5. Clique em **Criar** e escolha **Somente eu**.

Se a sua conta também não permitir criar GPTs, crie um **Projeto** e cole as instruções nas configurações dele, ou cole o conteúdo do arquivo como primeira mensagem de uma conversa nova (vale só para aquela conversa).

## Use

Escreva normalmente sobre a disciplina. Exemplos:

- "Não entendi o que é cardinalidade no DER."
- "Gere um simulado da A1."
- "Tirei 2,5 na A2. Quanto preciso na A1 para passar?"

## Problemas comuns

| O que acontece | O que fazer |
|---|---|
| O tutor diz que não consegue abrir o índice ou o material | Confira se a pesquisa na web está disponível. Se continuar, anexe à conversa o arquivo que ele pedir (você o encontra na pasta da disciplina no Drive). |
| O tutor responde, mas não cita o material | Peça: "Consulte o material da disciplina e cite o documento e a seção." |
| Ele resolve o trabalho por você | Não deveria. Avise o professor, com o print da conversa. |

## Atualizações

O tutor lê o material novo pela internet, então **você não precisa reinstalar** quando o professor publica uma aula. Reinstale só quando o professor avisar que saiu uma nova versão: envie o `.zip` novo pedindo para substituir a skill antiga, ou troque o texto das instruções do GPT em **Editar**.
