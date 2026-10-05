# Tutores IA UNICID

Tutores virtuais das disciplinas do **Prof. Cid R. Andrade (UNICID)**, empacotados como *skills* que funcionam no **Claude**, no **ChatGPT** e no **Gemini**.

> 🚧 **Em construção.** Os tutores ainda não estão prontos para uso. Os guias de instalação e os pacotes para download serão publicados na primeira versão (v1.0).

## O que é

Cada tutor é um monitor virtual da disciplina que:

- ajuda o aluno a entender o conteúdo pelo método socrático (pergunta, guia e só depois explica);
- consulta o material oficial da disciplina e cita documento e seção;
- gera simulados no formato das avaliações;
- explica a regra de aprovação;
- **não** resolve trabalhos avaliativos.

## Disciplinas

| Sigla | Disciplina | Skill |
|---|---|---|
| `dfw` | Desenvolvimento Front-End para Web | `tutor-dfw` |
| `dp` | Design Profissional | `tutor-design-profissional` |
| `ed2` | Estruturas de Dados II | `tutor-ed2` |
| `mbd` | Modelagem de Banco de Dados | `tutor-mbd` |
| `plp` | Paradigmas de Linguagens de Programação | `tutor-plp` |

## Como funciona

1. **Núcleo** (dentro da skill): persona, método, regras e avaliação. Muda raramente.
2. **Índice** (`indices/<sigla>.md` neste repositório): lista do material de cada semana, atualizada pelo professor. A skill lê o índice pela internet, então o aluno **não precisa reinstalar** quando entra material novo.
3. **Material** (pastas públicas no Google Drive): apostilas, slides e PDFs.

## Licenças

Este repositório usa duas licenças:

| Conteúdo | Licença |
|---|---|
| Textos didáticos: skills (`SKILL.md`, `references/`), índices, README e documentação | [CC BY-NC-SA 4.0](LICENSE) |
| Código em `scripts/` | [MIT](scripts/LICENSE) |

**Materiais de terceiros:** livros, apostilas, slides e demais arquivos nas pastas do Google Drive **não** fazem parte deste repositório e **não** são cobertos por estas licenças. Os direitos pertencem aos respectivos autores. Este repositório contém apenas títulos, resumos de autoria própria e links.

## Documentação do projeto

- [Decisões do projeto](docs/projeto/DECISOES_tutores-skills.md)
- [Roteiro de desenvolvimento](docs/projeto/ROTEIRO_ClaudeCode_tutores-skills.md)
