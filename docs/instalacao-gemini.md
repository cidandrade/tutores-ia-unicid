# Como instalar o tutor no Gemini

O Gemini está trocando os **Gems** por **skills** no formato aberto Agent Skills, o mesmo do Claude. A liberação começou em 30/09/2026 na web e chega ao app em 13/10/2026; em 17/11/2026 os Gems saem do menu principal e viram rascunhos de skills. Por isso há duas opções. Leva uns 5 minutos.

## Opção 1 — Skill (se já aparecer na sua conta)

1. Baixe o `.zip` da sua disciplina na [tabela do README](../README.md#disciplinas).
2. Em [gemini.google.com](https://gemini.google.com), procure **Skills** no menu da esquerda ou nas configurações.
3. Crie uma skill nova enviando o `.zip`. Se o Gemini não aceitar o `.zip`, descompacte-o e envie o arquivo `SKILL.md` e os arquivos da pasta `references/` como arquivos da skill.
4. Abra uma conversa nova e escreva sobre a disciplina.

> Ainda não está confirmado que o Gemini aceita o `.zip` do Claude sem ajuste. Se não der certo, use a Opção 2 e avise o professor do que aconteceu.

## Opção 2 — Gem

1. Baixe o arquivo `tutor-<sigla>-instrucoes.md` da sua disciplina na [tabela do README](../README.md#disciplinas) e abra-o num editor de texto.
2. Em [gemini.google.com](https://gemini.google.com), clique em **Explorar Gems** (ou **Gerenciador de Gems**) → **Novo Gem**.
3. Preencha:
   - **Nome:** o nome da disciplina, por exemplo "Tutor de Modelagem de Banco de Dados".
   - **Instruções:** cole **todo** o conteúdo do arquivo de instruções, sem cortar nada.
4. Clique em **Salvar**.

> Não use o botão que reescreve as instruções com IA: ele pode tirar regras importantes do tutor.

Depois de 17/11/2026, o Gem vira um rascunho de skill: abra-o em **Skills** e salve para continuar usando.

## Use

Escreva normalmente sobre a disciplina. Exemplos:

- "Não entendi o que é cardinalidade no DER."
- "Gere um simulado da A1."
- "Tirei 2,5 na A2. Quanto preciso na A1 para passar?"

## Material da disciplina

O Gemini nem sempre consegue abrir links da internet. Quando o tutor não conseguir ler um arquivo, ele vai pedir que você o anexe, por exemplo: "Pode anexar a Apostila 05?". Nesse caso, clique no **+** da caixa de mensagem → **Drive** (ou **Enviar arquivo**) e escolha o arquivo pedido na pasta da disciplina.

Você também pode anexar o material à própria skill ou ao Gem, para não repetir isso a cada conversa. Lembre-se de atualizar o anexo quando o professor publicar uma versão nova do arquivo.

## Problemas comuns

| O que acontece | O que fazer |
|---|---|
| O tutor diz que não consegue abrir o índice ou o material | É normal no Gemini. Anexe o arquivo que ele pedir. |
| O tutor responde, mas não cita o material | Peça: "Consulte o material da disciplina e cite o documento e a seção." Se ele não conseguir abrir, anexe o arquivo. |
| Ele resolve o trabalho por você | Não deveria. Avise o professor, com o print da conversa. |

## Atualizações

Quando o tutor consegue ler o índice pela internet, você **não precisa reinstalar** a cada aula nova. Reinstale só quando o professor avisar que saiu uma nova versão: envie o `.zip` novo (Opção 1) ou troque o texto das instruções do Gem em **Editar** (Opção 2).
