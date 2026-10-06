# Tutores IA UNICID

Tutores virtuais das disciplinas do **Prof. Cid R. Andrade (UNICID)**, no formato aberto **Agent Skills**: funcionam no **Claude**, no **ChatGPT**, no **Gemini** e em outras IAs.

## O que é

Cada tutor é um monitor virtual da disciplina que:

- ajuda você a entender o conteúdo pelo método socrático (pergunta, guia e só depois explica);
- consulta o material oficial da disciplina e cita documento e seção;
- gera simulados no formato das avaliações (A1, A2 e AF);
- explica a regra de aprovação e calcula quanto você precisa tirar;
- **não** resolve trabalhos avaliativos.

## Disciplinas

Baixe o arquivo da sua disciplina e siga o guia da sua IA. Use a **skill** (`.zip`) sempre que a IA aceitar; as **instruções** (`.md`) são para colar onde ela não aceita.

| Disciplina | Skill (.zip) | Instruções (.md) |
|---|---|---|
| Design Profissional | [tutor-design-profissional.zip](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-design-profissional.zip) | [tutor-design-profissional-instrucoes.md](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-design-profissional-instrucoes.md) |
| Desenvolvimento Front-End para Web | [tutor-dfw.zip](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-dfw.zip) | [tutor-dfw-instrucoes.md](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-dfw-instrucoes.md) |
| Estruturas de Dados II | [tutor-ed2.zip](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-ed2.zip) | [tutor-ed2-instrucoes.md](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-ed2-instrucoes.md) |
| Modelagem de Banco de Dados | [tutor-mbd.zip](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-mbd.zip) | [tutor-mbd-instrucoes.md](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-mbd-instrucoes.md) |
| Paradigmas de Linguagens de Programação | [tutor-plp.zip](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-plp.zip) | [tutor-plp-instrucoes.md](https://github.com/cidandrade/tutores-ia-unicid/releases/latest/download/tutor-plp-instrucoes.md) |

Todas as versões ficam em [Releases](https://github.com/cidandrade/tutores-ia-unicid/releases).

## Como instalar

1. [Claude](docs/instalacao-claude.md): envie o `.zip` em Personalização → Habilidades.
2. [ChatGPT](docs/instalacao-chatgpt.md): anexe o `.zip` numa conversa e peça "Instale esta skill" (ou crie um GPT com as instruções).
3. [Gemini](docs/instalacao-gemini.md): crie uma skill com o `.zip` (ou um Gem com as instruções).

### Outras IAs

| IA | Como usar o tutor |
|---|---|
| Manus | Envie o `.zip` como skill e chame com `/tutor-<sigla>` (ex.: `/tutor-mbd`). |
| Grok | Importe o `.zip` em Grok Skills. |
| Perplexity | Só no Perplexity Computer (o agente, que consome créditos): envie o `.zip`. Na busca comum, não há skills. |
| DeepSeek | Não aceita skills. Cole o conteúdo do arquivo de instruções como primeira mensagem de uma conversa nova. |
| Outras (Copilot, Cursor etc.) | Se aceitar Agent Skills (`SKILL.md`), use o `.zip`. Se não, cole as instruções no campo de instruções personalizadas ou na primeira mensagem. |

Para o tutor ler o material, a IA precisa conseguir abrir links da internet; se não conseguir, ele vai pedir que você anexe o arquivo.

## Como usar

Escreva normalmente sobre a disciplina, como faria com um monitor:

- "Não entendi o que é normalização. Pode me ajudar?"
- "Qual material fala de árvores AVL?"
- "Gere um simulado da A1."
- "Tirei 2,5 na A2. Quanto preciso na A1 para passar?"

O tutor vai começar perguntando o que você já sabe. Isso é de propósito: a ideia é você aprender, não receber a resposta pronta. Ele também não escreve trabalhos da A2 nem resolve questões de prova, mesmo que você diga que é só para conferir.

> O tutor pode errar. Em caso de dúvida, confira no material da disciplina ou pergunte ao professor.

## Como funciona

1. **Núcleo** (dentro do tutor): persona, método, regras, ementa e avaliação. Muda pouco.
2. **Índice** (`indices/<sigla>.md` neste repositório): lista do material de cada semana, atualizada pelo professor. O tutor lê o índice pela internet, então você **não precisa reinstalar** quando entra material novo.
3. **Material** (pastas públicas no Google Drive): apostilas, slides e PDFs.

Reinstale só quando o professor avisar que saiu uma nova versão.

## Licenças

Este repositório usa duas licenças:

| Conteúdo | Licença |
|---|---|
| Textos didáticos: skills (`SKILL.md`, `references/`), instruções, índices, README e documentação | [CC BY-NC-SA 4.0](LICENSE) |
| Código em `scripts/` | [MIT](scripts/LICENSE) |

**Materiais de terceiros:** livros, apostilas, slides e demais arquivos nas pastas do Google Drive **não** fazem parte deste repositório e **não** são cobertos por estas licenças. Os direitos pertencem aos respectivos autores. Este repositório contém apenas títulos, resumos de autoria própria e links.

**Marcas:** Claude, ChatGPT, Gemini e os demais nomes citados pertencem às respectivas empresas. Este projeto não tem vínculo com elas.

## Para o professor

- [Decisões do projeto](docs/projeto/DECISOES_tutores-skills.md)
- [Roteiro de desenvolvimento](docs/projeto/ROTEIRO_ClaudeCode_tutores-skills.md)
- [Checklist de testes](docs/projeto/PILOTO_checklist-dp.md)
- Rotina semanal: atualizar o Drive, rodar `/atualizar-indice` no Claude Code, revisar o diff e fazer commit e push.
