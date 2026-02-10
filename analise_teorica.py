import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
#  QUESTÃO D: ANÁLISE TEÓRICA DA COMPLEXIDADE T(n)
# ============================================================================
#  Este script valida o cálculo teórico de T(n) comparando as curvas
#  matemáticas ideais com os dados coletados no experimento.
#
#  Modelo Matemático (Linear):
#  T(n) = a * n + b
#  Onde:
#    'n' é o tamanho da entrada.
#    'a' é o tempo de processamento por item (inclinação).
#    'b' é o tempo constante de inicialização (intercepto).
# ============================================================================

# --- 1. DADOS OBTIDOS (Do Benchmark) ---
n_elementos = [100_000, 1_000_000, 5_000_000, 10_000_000, 50_000_000]

# Tempos médios (em milissegundos)
tempos_exp_for = [15.2, 152.7, 761.9, 1523.4, 7617.9]
tempos_exp_lambda = [21.4, 215.3, 1076.5, 2154.3, 10769.2]

# --- 2. CÁLCULO DOS COEFICIENTES TEÓRICOS ---
# Para encontrar a equação da reta T(n) = an + b, usamos regressão linear simples
# ou uma aproximação baseada na média (tempo / n).

# Coeficiente angular 'a' (nanosegundos por elemento)
# Calculado dividindo o tempo total pelo número de elementos (média dos casos grandes)
a_for = 0.0001523      # ~152 ns/elemento
a_lambda = 0.0002154   # ~215 ns/elemento

# Coeficiente linear 'b' (milissegundos)
# Representa o custo fixo (sleep + alocação inicial)
b_for = 0.1 
b_lambda = 0.15

def plotar_analise_teorica():
    """
    Gera o gráfico comparativo entre a Teoria O(n) e a Prática.
    """
    # Cria uma sequência contínua de N para desenhar a linha teórica perfeita
    n_teorico = np.linspace(min(n_elementos), max(n_elementos), 100)
    
    # Aplica a fórmula T(n) = an + b
    t_teorico_for = a_for * n_teorico + b_for
    t_teorico_lambda = a_lambda * n_teorico + b_lambda
    
    # Configuração do Gráfico
    plt.figure(figsize=(10, 7))
    
    # 1. Plota as Linhas Teóricas (Matemática)
    plt.plot(n_teorico, t_teorico_for, 'b--', linewidth=1.5, alpha=0.7, label='Teoria T(n) For')
    plt.plot(n_teorico, t_teorico_lambda, 'r--', linewidth=1.5, alpha=0.7, label='Teoria T(n) Lambda')
    
    # 2. Plota os Pontos Experimentais (Realidade)
    plt.plot(n_elementos, tempos_exp_for, 'bo', markersize=8, label='Dados Reais (For)')
    plt.plot(n_elementos, tempos_exp_lambda, 'rs', markersize=8, label='Dados Reais (Lambda)')
    
    # Decoração
    plt.title('Validação da Análise Teórica: T(n) = O(n)', fontsize=14, fontweight='bold')
    plt.xlabel('Tamanho da Entrada (n)', fontsize=12)
    plt.ylabel('Tempo (ms)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ticklabel_format(style='plain', axis='x')
    
    # Adiciona o texto das fórmulas no gráfico
    texto_formulas = (
        f"Fórmulas Calculadas:\n"
        f"For:      T(n) ≈ {a_for:.7f}n + {b_for}\n"
        f"Lambda: T(n) ≈ {a_lambda:.7f}n + {b_lambda}"
    )
    plt.text(0.05, 0.85, texto_formulas, transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray'))
    
    plt.tight_layout()
    plt.show()

# ============================================================================
#  EXECUÇÃO
# ============================================================================
if __name__ == "__main__":
    print(f"{'='*60}")
    print(f"{'ANÁLISE TEÓRICA DE COMPLEXIDADE':^60}")
    print(f"{'='*60}")
    print(f"Modelo Matemático Identificado: Linear O(n)\n")
    print(f"Equação do Loop For:   T(n) = {a_for:.7f} * n + {b_for}")
    print(f"Equação do Lambda:     T(n) = {a_lambda:.7f} * n + {b_lambda}")
    print(f"{'-'*60}")
    print("Gerando gráfico de validação...")
    
    plotar_analise_teorica()