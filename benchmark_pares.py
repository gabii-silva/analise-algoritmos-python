import time

# ============================================================================
#  PROJETO: BENCHMARK DE PERFORMANCE (PYTHON)
# ============================================================================
#  Este script compara o tempo de execucao de duas abordagens para 
#  filtrar numeros pares em uma lista de dados.
#
#  Cenarios Testados:
#  1. Iteracao Classica (Loop For)
#  2. Programacao Funcional (Lambda + Filter)
# ============================================================================

# --- Configuracao dos Dados (Mock Data / Inputs) ---
# Definimos diferentes tamanhos de lista para testar a escalabilidade
entradas = [10**5, 10**6, 5*10**6, 10**7] 

def numpares(l):
    """
    Logica 1: Abordagem Imperativa (Classica)
    Cria uma lista vazia e itera item a item manualmente.
    """
    inicio = time.time()        # Marca o tempo inicial (t0)
    time.sleep(0.5)             # Pausa artificial (simula carga constante)
    
    pares = []                  # Inicializa lista vazia na memoria
    
    # --- Processamento do Loop (Iteracao) ---
    for i in l:
        if i % 2 == 0:          # Criterio 1: Verifica se o resto da divisao e 0
            pares.append(i)     # Acao: Adiciona o numero a lista final
            
    fim = time.time()           # Marca o tempo final (t1)
    
    # Formatacao do tempo
    tempo_total = fim - inicio
    print(f'For Loop | N={len(l):.0e}: {tempo_total:.4f}s')
    return tempo_total

def numparesL(l):
    """
    Logica 2: Abordagem Funcional (Pythonic)
    Utiliza funcoes de alta ordem (filter) com funcoes anonimas (lambda).
    """
    inicio = time.time()        # Marca o tempo inicial
    time.sleep(0.5)             # Pausa artificial
    
    # --- Processamento Funcional (Linha unica) ---
    # filter() aplica a regra a cada item. list() materializa o resultado.
    pares = list(filter(lambda valor: valor % 2 == 0, l))
    
    fim = time.time()           # Marca o tempo final
    
    # Formatacao do tempo
    tempo_total = fim - inicio
    print(f'Lambda   | N={len(l):.0e}: {tempo_total:.4f}s')
    return tempo_total

# ============================================================================
#  EXECUCAO PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    
    print("="*60)
    print("INICIANDO COMPARACAO: For Loop vs Lambda")
    print("="*60)
    
    # Listas para armazenar resultados e gerar relatorio final
    tempos_for = []
    tempos_lambda = []

    # --- Loop de Testes (Varios Cenarios) ---
    for n in entradas:
        print(f"\n---> Testando com N={n:,} elementos:")
        
        # Preparacao dos dados (Gera a lista na memoria RAM)
        lista_teste = list(range(n))
        
        # 1. Executa Logica Imperativa
        tempo_for = numpares(lista_teste)
        tempos_for.append(tempo_for)
        
        # 2. Executa Logica Funcional
        tempo_lambda = numparesL(lista_teste)
        tempos_lambda.append(tempo_lambda)

    # --- Relatorio Final (Output Formatado) ---
    print("\n" + "="*60)
    print(f"{'Tamanho (N)':<15} {'For Loop (s)':<15} {'Lambda (s)':<15} {'Diferenca':<15}")
    print("="*60)

    for i, n in enumerate(entradas):
        # Calculo da diferenca de performance
        diff = tempos_lambda[i] - tempos_for[i]
        
        # Define se o resultado foi positivo ou negativo visualmente
        sinal = "+" if diff > 0 else "" 
        
        # Exibe a linha da tabela
        print(f"{n:<15,} {tempos_for[i]:<15.4f} {tempos_lambda[i]:<15.4f} {sinal}{diff:<14.4f}s")