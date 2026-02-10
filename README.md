# 📊 Análise de Complexidade e Performance: Loops vs. Lambda em Python

Este projeto realiza uma **análise comparativa completa** (teórica e experimental) entre duas abordagens de iteração em Python: o laço imperativo (`for`) e a abordagem funcional (`filter` + `lambda`).

O estudo valida matematicamente a complexidade assintótica $O(n)$ e analisa o overhead de chamadas de função em Python através de testes de estresse com até **50 milhões de elementos**.

## 🎯 Objetivos

- **Benchmark:** Comparação de tempo de execução variando $N$ de $10^5$ a $5 \cdot 10^7$.
- **Modelagem Teórica:** Validação da hipótese linear $T(n) = a \cdot n + b$.
- **Análise Visual:** Geração de dashboards com `matplotlib` (resíduos, escala log-log e coeficientes).

## 📂 Estrutura do Projeto

| Arquivo | Descrição |
| :--- | :--- |
| `analise_completa.py` | **Script Principal.** Gera o relatório final com dashboard de 4 gráficos (Teórico vs Prático). |
| `benchmark_completo.py` | Executa o teste de carga pesada e imprime os tempos brutos. |
| `analise_teorica.py` | Plota as curvas teóricas ideais sobrepostas aos dados reais para validação $O(n)$. |
| `analise_experimental.py` | Foca na comparação direta (razão de tempos e diferença percentual). |
| `benchmark_pares.py` | Script inicial para testes rápidos de menor escala. |

## 🚀 Como Executar

1. Instale as dependências:
   ```bash
   pip install matplotlib numpy

   Execute a mágica ✨
python analise_completa.py