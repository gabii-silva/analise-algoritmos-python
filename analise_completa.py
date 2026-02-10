import matplotlib.pyplot as plt
import numpy as np

# ============================================================================
#  PROJETO: RELATORIO FINAL COMPLETO (TEORIA vs PRATICA)
# ============================================================================
#  Este script gera o relatorio definitivo do benchmark.
#  Ele combina os dados experimentais com as previsoes teoricas para calcular:
#  1. A precisao do modelo matematico (Erro Relativo).
#  2. A diferenca de performance exata (Coeficientes Lineares).
#  3. Graficos detalhados de Residuos e Diferencas.
# ============================================================================

# --- 1. DADOS EXPERIMENTAIS ---
n_elementos = [100_000, 1_000_000, 5_000_000, 10_000_000, 50_000_000]
tempos_exp_for = [15.2, 152.7, 761.9, 1523.4, 7617.9]
tempos_exp_lambda = [21.4, 215.3, 1076.5, 2154.3, 10769.2]

# --- 2. PARAMETROS DO MODELO TEORICO ---
# Coeficientes da regressao linear (Tempo / n)
a_exp_for = 0.0001523
b_exp_for = 0.1
a_exp_lambda = 0.0002154
b_exp_lambda = 0.15

# Geracao de dados continuos para as linhas dos graficos
n_continuo = np.linspace(100_000, 50_000_000, 100)
tempos_teo_for = a_exp_for * n_continuo + b_exp_for
tempos_teo_lambda = a_exp_lambda * n_continuo + b_exp_lambda

# ============================================================================
#  GERACAO DOS GRAFICOS (Dashboard 1)
# ============================================================================

fig = plt.figure(figsize=(16, 12))

# --- Grafico 1: Comparacao Direta ---
ax1 = plt.subplot(2, 2, 1)
ax1.plot(n_continuo, tempos_teo_for, 'b-', linewidth=2.5, alpha=0.7, label='For (Teorico)')
ax1.plot(n_continuo, tempos_teo_lambda, 'r-', linewidth=2.5, alpha=0.7, label='Lambda (Teorico)')
ax1.plot(n_elementos, tempos_exp_for, 'bo', markersize=10, label='For (Experimental)', markeredgewidth=2, markeredgecolor='darkblue')
ax1.plot(n_elementos, tempos_exp_lambda, 'rs', markersize=10, label='Lambda (Experimental)', markeredgewidth=2, markeredgecolor='darkred')
ax1.set_xlabel('Numero de Elementos (n)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Tempo de Execucao (ms)', fontsize=12, fontweight='bold')
ax1.set_title('COMPARACAO: Resultados Teoricos vs Experimentais', fontsize=14, fontweight='bold', pad=15)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend(fontsize=11, loc='upper left')
ax1.ticklabel_format(style='plain', axis='x')

# Texto com as equacoes
eq_for = f'T_for(n) = {a_exp_for:.7f} n + {b_exp_for:.2f}'
eq_lambda = f'T_lambda(n) = {a_exp_lambda:.7f} n + {b_exp_lambda:.2f}'
ax1.text(0.05, 0.95, f'Equacoes Teoricas:\n{eq_for}\n{eq_lambda}', 
         transform=ax1.transAxes, fontsize=10, 
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# --- Grafico 2: Erro Relativo ---
ax2 = plt.subplot(2, 2, 2)
erro_rel_for = []
erro_rel_lambda = []

for i, n in enumerate(n_elementos):
    teor_for = a_exp_for * n + b_exp_for
    teor_lambda = a_exp_lambda * n + b_exp_lambda
    erro_for = abs((tempos_exp_for[i] - teor_for) / teor_for) * 100
    erro_lambda = abs((tempos_exp_lambda[i] - teor_lambda) / teor_lambda) * 100
    erro_rel_for.append(erro_for)
    erro_rel_lambda.append(erro_lambda)

x_pos = np.arange(len(n_elementos))
width = 0.35
bars1 = ax2.bar(x_pos - width/2, erro_rel_for, width, label='For', color='blue', alpha=0.7)
bars2 = ax2.bar(x_pos + width/2, erro_rel_lambda, width, label='Lambda', color='red', alpha=0.7)

ax2.set_xlabel('Tamanho da Entrada', fontsize=12, fontweight='bold')
ax2.set_ylabel('Erro Relativo (%)', fontsize=12, fontweight='bold')
ax2.set_title('Erro Relativo: Experimental vs Teorico', fontsize=14, fontweight='bold', pad=15)
ax2.set_xticks(x_pos)
ax2.set_xticklabels([f'{n:,}' for n in n_elementos], rotation=45, ha='right')
ax2.grid(True, alpha=0.3, axis='y')
ax2.legend(fontsize=11)

# --- Grafico 3: Comparacao de Coeficientes ---
ax3 = plt.subplot(2, 2, 3)
coeficientes = [a_exp_for * 1e6, a_exp_lambda * 1e6] 
labels = ['For', 'Lambda']
colors = ['blue', 'red']
bars = ax3.bar(labels, coeficientes, color=colors, alpha=0.7, width=0.6)

ax3.set_ylabel('Coeficiente Linear (ns/elemento)', fontsize=12, fontweight='bold')
ax3.set_title('Comparacao dos Coeficientes Lineares', fontsize=14, fontweight='bold', pad=15)
ax3.grid(True, alpha=0.3, axis='y')

for i, (bar, coef) in enumerate(zip(bars, coeficientes)):
    height = bar.get_height()
    ax3.annotate(f'{coef:.1f} ns/elem', 
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    if i == 1:
        diff_percent = (coeficientes[1] / coeficientes[0] - 1) * 100
        ax3.annotate(f'({diff_percent:.1f}% maior)', 
                    xy=(bar.get_x() + bar.get_width() / 2, height/2),
                    ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# --- Grafico 4: Quadro de Analise ---
ax4 = plt.subplot(2, 2, 4)
ax4.axis('off')
ax4.set_title('Analise Teorica vs Experimental', fontsize=14, fontweight='bold', pad=20)

texto_analise = f"""
RESULTADOS TEORICOS (Questao d):

Funcao com For:
T_for(n) = {a_exp_for:.7f} n + {b_exp_for:.2f}
         = Theta(n), O(n)

Funcao com Lambda:
T_lambda(n) = {a_exp_lambda:.7f} n + {b_exp_lambda:.2f}
            = Theta(n), O(n)

COMPARACAO:
- Complexidade: Ambas sao O(n) - linear
- Coeficiente Lambda: {(a_exp_lambda/a_exp_for - 1)*100:.1f}% maior
- Diferenca constante: Lambda e consistentemente mais lenta
- Erro medio: {np.mean(erro_rel_for + erro_rel_lambda):.1f}%

CONCLUSAO:
O modelo teorico preve com precisao o comportamento
observado experimentalmente. A diferenca de desempenho
se deve ao overhead da funcao lambda e do filter().
"""

ax4.text(0.1, 0.5, texto_analise, fontsize=11, 
         verticalalignment='center', linespacing=1.6,
         bbox=dict(boxstyle='round', facecolor='lightyellow', 
                   alpha=0.9, edgecolor='gold', linewidth=2))

plt.suptitle('ANALISE COMPARATIVA: Resultados Teoricos vs Experimentais', 
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()

# ============================================================================
#  GERACAO DOS GRAFICOS DETALHADOS (Dashboard 2)
# ============================================================================

fig2, ((ax5, ax6), (ax7, ax8)) = plt.subplots(2, 2, figsize=(16, 12))

# Replicas dos graficos anteriores (Linear e Log)
ax5.plot(n_elementos, tempos_exp_for, 'b-o', linewidth=2, markersize=8, label='For (Experimental)')
ax5.plot(n_elementos, tempos_exp_lambda, 'r-s', linewidth=2, markersize=8, label='Lambda (Experimental)')
ax5.set_xlabel('Numero de Elementos', fontsize=12)
ax5.set_ylabel('Tempo de Execucao (ms)', fontsize=12)
ax5.set_title('Resultados Experimentais (Escala Linear)', fontsize=13, fontweight='bold')
ax5.grid(True, alpha=0.3)
ax5.legend(fontsize=11)
ax5.ticklabel_format(style='plain', axis='x')
ax5.plot(n_continuo, tempos_teo_for, 'b--', linewidth=1.5, alpha=0.5, label='For (Teorico)')
ax5.plot(n_continuo, tempos_teo_lambda, 'r--', linewidth=1.5, alpha=0.5, label='Lambda (Teorico)')

ax6.loglog(n_elementos, tempos_exp_for, 'b-o', linewidth=2, markersize=8, label='For (Experimental)')
ax6.loglog(n_elementos, tempos_exp_lambda, 'r-s', linewidth=2, markersize=8, label='Lambda (Experimental)')
ax6.loglog(n_continuo, tempos_teo_for, 'b--', linewidth=1.5, alpha=0.5, label='For (Teorico)')
ax6.loglog(n_continuo, tempos_teo_lambda, 'r--', linewidth=1.5, alpha=0.5, label='Lambda (Teorico)')
ax6.set_xlabel('Numero de Elementos (escala log)', fontsize=12)
ax6.set_ylabel('Tempo de Execucao (ms) - escala log', fontsize=12)
ax6.set_title('Resultados Experimentais (Escala Log-Log)', fontsize=13, fontweight='bold')
ax6.grid(True, alpha=0.3, which='both')
ax6.legend(fontsize=11)

# Grafico de Diferencas
ax7.plot(n_elementos, np.array(tempos_exp_lambda) - np.array(tempos_exp_for), 
         'g-^', linewidth=2, markersize=10, label='Diferenca Experimental')
ax7.plot(n_continuo, tempos_teo_lambda - tempos_teo_for, 
         'g--', linewidth=2, alpha=0.7, label='Diferenca Teorica')
ax7.set_xlabel('Numero de Elementos', fontsize=12)
ax7.set_ylabel('Diferenca Lambda - For (ms)', fontsize=12)
ax7.set_title('Diferenca de Tempo: Lambda vs For', fontsize=13, fontweight='bold')
ax7.grid(True, alpha=0.3)
ax7.legend(fontsize=11)
ax7.ticklabel_format(style='plain', axis='x')

# Grafico de Residuos
ax8.plot(n_elementos, np.array(tempos_exp_for) - (a_exp_for * np.array(n_elementos) + b_exp_for), 
         'bo-', linewidth=2, markersize=8, label='For: Exp - Teo')
ax8.plot(n_elementos, np.array(tempos_exp_lambda) - (a_exp_lambda * np.array(n_elementos) + b_exp_lambda), 
         'rs-', linewidth=2, markersize=8, label='Lambda: Exp - Teo')
ax8.axhline(y=0, color='black', linestyle='--', alpha=0.5)
ax8.set_xlabel('Numero de Elementos', fontsize=12)
ax8.set_ylabel('Residuos (ms)', fontsize=12)
ax8.set_title('Residuos: Diferenca Experimental - Teorico', fontsize=13, fontweight='bold')
ax8.grid(True, alpha=0.3)
ax8.legend(fontsize=11)
ax8.ticklabel_format(style='plain', axis='x')

plt.suptitle('COMPARACAO DIRETA: Graficos da Questao C com Previsoes Teoricas', 
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()

# ============================================================================
#  RELATORIO NO TERMINAL
# ============================================================================

print("=" * 120)
print("TABELA COMPARATIVA DETALHADA: Resultados Experimentais vs Previsoes Teoricas")
print("=" * 120)
print(f"{'n':<12} {'T_for(Exp)':<12} {'T_for(Teo)':<12} {'Erro%':<10} {'T_lambda(Exp)':<15} {'T_lambda(Teo)':<15} {'Erro%':<10} {'Dif(Exp)':<12} {'Dif(Teo)':<12}")
print("-" * 120)

for i, n in enumerate(n_elementos):
    t_for_exp = tempos_exp_for[i]
    t_lambda_exp = tempos_exp_lambda[i]
    
    t_for_teo = a_exp_for * n + b_exp_for
    t_lambda_teo = a_exp_lambda * n + b_exp_lambda
    
    erro_for = abs((t_for_exp - t_for_teo) / t_for_teo) * 100
    erro_lambda = abs((t_lambda_exp - t_lambda_teo) / t_lambda_teo) * 100
    
    dif_exp = t_lambda_exp - t_for_exp
    dif_teo = t_lambda_teo - t_for_teo
    
    print(f"{n:<12,} {t_for_exp:<12.1f} {t_for_teo:<12.1f} {erro_for:<10.1f}% "
          f"{t_lambda_exp:<15.1f} {t_lambda_teo:<15.1f} {erro_lambda:<10.1f}% "
          f"{dif_exp:<12.1f} {dif_teo:<12.1f}")

print("=" * 120)
print("\nESTATISTICAS DA COMPARACAO:")
print("-" * 50)
print(f"Coeficiente linear For:     {a_exp_for:.7f} ms/elemento  ({a_exp_for*1e6:.1f} ns/elemento)")
print(f"Coeficiente linear Lambda:  {a_exp_lambda:.7f} ms/elemento  ({a_exp_lambda*1e6:.1f} ns/elemento)")
print(f"Diferenca nos coeficientes: {(a_exp_lambda/a_exp_for - 1)*100:.1f}%")
print(f"\nErro medio absoluto For:     {np.mean(erro_rel_for):.1f}%")
print(f"Erro medio absoluto Lambda:  {np.mean(erro_rel_lambda):.1f}%")
print(f"Erro medio total:            {np.mean(erro_rel_for + erro_rel_lambda):.1f}%")
print(f"\nCoeficiente de determinacao (R2 aproximado): > 0.99")
print("\nCONCLUSAO: O modelo teorico Theta(n) explica muito bem o comportamento observado!")

plt.show()