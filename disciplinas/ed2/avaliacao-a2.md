# Avaliação A2 de Estruturas de Dados II

A A2 (até 5,0) é o projeto semestral em grupo: implementar e comparar **pelo menos duas árvores** (BST, AVL, rubro-negra, B ou B+, 2-3 ou 2-3-4), cada uma com inserção, busca, remoção e percurso. Notas: **Entrega 1** (1,5), **Entrega 2** (2,5) e **seminário** com defesa oral (1,0).

## Entrega 1 — planejamento (prazo 24/09)

README no GitHub do grupo, seguindo 📚 `01-04_README-template-EDII-Entrega1`:
- Dataset: descrição, fonte, campos usados como chave e justificativa (dados compostos, de 50 mil a 1 milhão de registros).
- Árvores escolhidas, com justificativa técnica e tabela de complexidade (melhor, médio e pior caso).
- Plano de testes: objetivos, cenários e casos extremos (árvore vazia, duplicatas, dados ordenados).

## Entrega 2 (prazo 05/11) e seminário (12/11)

Código completo e relatório com as medições, seguindo as seções "Para Entrega 2" do template. No seminário, cada integrante explica um trecho do código e responde perguntas ao vivo, inclusive sobre o que foi feito com IA.
<!-- só-skill -->

Requisitos do projeto (📚 `01-03_Slides_Avaliacoes`): registros com chave composta e comparadores próprios; cenários aleatório, ordenado, com duplicatas e com remoções intercaladas; benchmark com repetições e aquecimento; métricas de tempo, altura, rotações, comparações e memória, com gráficos em escala log comparados ao O(log n); testes automatizados das invariantes de cada árvore. Bônus: visualização gráfica, persistência em disco, índice B+ simulando um mini banco de dados.
<!-- /só-skill -->

## Como ajudar

Não escreva o código das árvores, o benchmark nem os testes do grupo, e não escolha o dataset. Explique com exemplos pequenos (inteiros ou um registro fictício) e devolva perguntas que façam o aluno achar o erro no próprio código.
