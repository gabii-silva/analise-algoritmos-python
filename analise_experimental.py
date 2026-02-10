import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
#  PROJETO: ANALISE EXPERIMENTAL DE DESEMPENHO
# ============================================================================
#  Este script gera graficos e tabelas estatisticas com base nos dados
#  coletados durante o benchmark (For Loop vs Lambda).
#
#  Saidas Geradas:
#  1. Tabela comparativa no terminal.
#  2. Graficos de linha (Escala Linear e Logaritmica).
#  3. Graficos de barra (Diferenca Percentual e Razao de Tempo).
# ============================================================================

# --- DADOS EXPERIMENTAIS (Hardcoded dos testes anteriores) ---
n_elementos = [100_000, 1_000_000, 5_000_000, 10_000_000, 50_000_000]

# Tempos medios em milissegundos (ms)
tempos_for = [15.2, 152.7, 761.9, 1523.4, 7617.9]
tempos_lambda = [21.4, 215.3, 1076.5, 2154.3, 10769.2]

def imprimir_relatorio(n_elems, t_for, t_lambda):
    """
    Calcula estatisticas e imprime a tabela de dados no terminal.
    """
    # Calculos estatisticos
    # List comprehension para calcular a diferenca % item a item
    diferenca_percentual = [(tl/tf - 1) * 100 for tf, tl in zip(t_for, t_lambda)]
    razao_tempos = [tl/tf for tf, tl in zip(t_for, t_lambda)]

    print("=" * 80)
    print("TABELA DE DADOS - Analise Experimental")
    print("=" * 80)
    print(f"{'N Elementos':<15} {'For (ms)':<12} {'Lambda (ms)':<15} {'Diferenca (ms)':<18} {'% Mais Lento':<15}")
    print("-" * 80)

    # Loop para imprimir linha por linha formatada
    for n, tf, tl in zip(n_elems, t_for, t_lambda):
        diferenca_ms = tl - tf
        percentual = (tl/tf - 1) * 100
        print(f"{n:<15,} {tf:<12.1f} {tl:<15.1f} {diferenca_ms:<18.1f} {percentual:<15.1f}%")

    print("=" * 80)
    print("\nRESUMO ESTATISTICO:")
    print(f"- Media diferenca percentual: {np.mean(diferenca_percentual):.1f}%")
    print(f"- Media razao Lambda/For: {np.mean(razao_tempos):.2f}x")
    print(f"- Comportamento: Ambas funcoes sao O(n) - crescimento linear")
    print(f"- Recomendacao: Use a funcao com 'for' para melhor desempenho")
    print("\n[AVISO] Feche as janelas dos graficos para encerrar o programa.")

    return diferenca_percentual, razao_tempos

def gerar_graficos(n_elems, t_for, t_lambda, diff_perc, razao):
    """
    Configura e exibe os graficos usando Matplotlib.
    """
    # --- FIGURA 1: Comparacao de Tempos (Linear e Log) ---
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Grafico Linear
    ax1.plot(n_elems, t_for, 'b-o', linewidth=2, markersize=8, label='Funcao com For')
    ax1.plot(n_elems, t_lambda, 'r-s', linewidth=2, markersize=8, label='Funcao com Lambda')
    ax1.set_xlabel('Numero de Elementos', fontsize=12)
    ax1.set_ylabel('Tempo de Execucao (ms)', fontsize=12)
    ax1.set_title('Comparacao de Tempo de Execucao\n(Escala Linear)', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=11)
    ax1.ticklabel_format(style='plain', axis='x')

    # Anotacoes nos pontos
    for x, y1, y2 in zip(n_elems, t_for, t_lambda):
        ax1.annotate(f'{y1:.1f}', (x, y1), textcoords="offset points", xytext=(0,10), 
                     ha='center', fontsize=9, color='blue')
        ax1.annotate(f'{y2:.1f}', (x, y2), textcoords="offset points", xytext=(0,-15), 
                     ha='center', fontsize=9, color='red')

    # Grafico Log-Log (Melhor para ver ordens de magnitude)
    ax2.loglog(n_elems, t_for, 'b-o', linewidth=2, markersize=8, label='Funcao com For')
    ax2.loglog(n_elems, t_lambda, 'r-s', linewidth=2, markersize=8, label='Funcao com Lambda')
    ax2.set_xlabel('Numero de Elementos (escala log)', fontsize=12)
    ax2.set_ylabel('Tempo de Execucao (ms) - escala log', fontsize=12)
    ax2.set_title('Comparacao de Tempo de Execucao\n(Escala Log-Log)', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, which='both')
    ax2.legend(fontsize=11)
    ax2.grid(True, which='minor', alpha=0.2)

    # --- FIGURA 2: Diferenca Percentual ---
    fig2, ax3 = plt.subplots(figsize=(10, 6))
    bars = ax3.bar(range(len(n_elems)), diff_perc, color='orange', alpha=0.7)
    ax3.set_xlabel('Tamanho da Entrada', fontsize=12)
    ax3.set_ylabel('Diferenca Percentual (%)', fontsize=12)
    ax3.set_title('Quanto a Funcao Lambda e Mais Lenta\n(em relacao a funcao For)', fontsize=14, fontweight='bold')
    ax3.set_xticks(range(len(n_elems)))
    ax3.set_xticklabels([f'{n:,}' for n in n_elems], rotation=45, ha='right')
    ax3.grid(True, alpha=0.3, axis='y')

    # Valores nas barras
    for bar, diff in zip(bars, diff_perc):
        height = bar.get_height()
        ax3.annotate(f'{diff:.1f}%', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

    # --- FIGURA 3: Razao de Crescimento ---
    fig3, ax4 = plt.subplots(figsize=(10, 6))
    x_pos = np.arange(len(n_elems))
    # Barras comparativas
    ax4.bar(x_pos - 0.2, [1] * len(n_elems), width=0.4, label='For (referencia)', color='blue', alpha=0.6)
    ax4.bar(x_pos + 0.2, razao, width=0.4, label='Lambda', color='red', alpha=0.6)
    
    ax4.set_xlabel('Tamanho da Entrada', fontsize=12)
    ax4.set_ylabel('Razao de Tempo (normalizado)', fontsize=12)
    ax4.set_title('Razao de Tempo de Execucao\n(Lambda vs For)', fontsize=14, fontweight='bold')
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels([f'{n:,}' for n in n_elems], rotation=45, ha='right')
    ax4.axhline(y=1, color='black', linestyle='--', alpha=0.5)
    ax4.legend(fontsize=11)
    ax4.grid(True, alpha=0.3, axis='y')

    # Texto nas barras
    for i, ratio in enumerate(razao):
        ax4.text(i + 0.2, ratio + 0.02, f'{ratio:.2f}x', 
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.show()

# ============================================================================
#  EXECUCAO PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    # 1. Processa dados e imprime tabela
    diff_perc, razao = imprimir_relatorio(n_elementos, tempos_for, tempos_lambda)
    
    # 2. Gera e mostra os graficos
    gerar_graficos(n_elementos, tempos_for, tempos_lambda, diff_perc, razao)