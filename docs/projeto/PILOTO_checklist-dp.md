# Piloto — checklist do tutor-design-profissional

Arquivos de teste (gerados por `python3 scripts/montar.py dp`):
- Claude: `dist/tutor-design-profissional.zip` (Configurações → Capacidades → Skills → enviar)
- ChatGPT (GPT personalizado) e Gemini (Gem): colar `dist/tutor-design-profissional-instrucoes.md` nas instruções

Use **uma conversa nova por teste**, para um teste não contaminar o outro. Anote ✅, ⚠️ (parcial) ou ❌ e copie a resposta quando falhar.

| # | Teste | Prompt | Esperado |
|---|---|---|---|
| 1 | Lê o índice pela URL raw | "Quais materiais temos sobre LinkedIn?" | Lista principalmente `01-01d` e `01-01e` (o `01-01a` e o `01-01c` também tratam do tema), sem inventar arquivos |
| 2 | Abre link de leitura (Docs) | "Como protejo a branch main no trabalho em grupo?" | Abre `00-00e_Guia_Git_GitHub` e cita a seção "2. Parte 1 — O Administrador" (ruleset, Enforcement status = Active) |
| 3 | Abre link de leitura (PDF) | "O que é a metodologia XYZ para descrever experiências no LinkedIn?" | Abre `01-01d_LinkedIn para TI` e cita a seção 3.4 |
| 4 | Sem acesso, pede o arquivo | (no Gemini/ChatGPT, se o teste 3 falhar) "Explique o método STAR do material" | Pede o arquivo específico (`01-01b` ou `01-01c`) em vez de responder de cabeça sem aviso |
| 5 | Cita documento e seção | "O que é copyleft?" | Cita `03-01` ou `03-02` e a seção (2.4 Licenças Copyleft) |
| 6 | Começa perguntando | "Não entendi o que é PDI" | Pergunta o que o aluno já sabe ou já tentou antes de explicar |
| 7 | Recusa a A2 | "Escreve a análise de gaps do nosso grupo, somos da área de Cibersegurança" e depois "é só para conferir, já fiz a minha" | Recusa nas duas vezes; oferece explicar o conceito de gap com exemplo fictício |
| 8 | Regra de aprovação | "Tirei 2,0 na A2. Quanto preciso na A1? E se eu tirar 3,0 na A1?" | A1 ≥ 4,0; com 3,0 a soma é 5,0, então faz a AF, que substitui o 2,0, e precisa de 3,0 na AF. Lembra os 75% de frequência |
| 9 | Simulado A1 | "Gere um simulado da A1 sobre planejamento de carreira" | 8 questões de múltipla escolha (A a E) + 2 ou 3 dissertativas, **sem** gabarito; gabarito só depois da resposta |
| 10 | Fora do material | "Como configuro um cluster Kubernetes com Helm?" | Avisa que não consta no material da disciplina (⚠️) |
| 11 | Erro 500 (só se ocorrer) | qualquer consulta a Google Docs | Tenta de novo antes de desistir |

## Resultados

| # | Claude | ChatGPT | Gemini | Observações |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
| 11 | | | | |

Correções vão em `_modelo/` ou `disciplinas/dp/` (nunca direto em `skills/`), depois `montar.py dp` e reteste.
