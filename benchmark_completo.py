import time

# ============================================================================
#  PROJETO: BENCHMARK DE PERFORMANCE (VERSÃO COMPLETA)
# ============================================================================
#  Este script realiza um teste de carga comparando duas abordagens para
#  filtrar números pares, incluindo testes de alto volume (50 milhões).
#
#  Cenários:
#  1. Abordagem Imperativa (Loop For)
#  2. Abordagem Funcional (Lambda + Filter)
# ============================================================================

def numpares(l):
    """
    Lógica 1: Abordagem Imperativa (Clássica)
    Percorre a lista item a item e verifica a condição.
    Complexidade: O(n)
    """
    inicio = time.time()        # Marca o tempo inicial (t0)
    time.sleep(0.5)             # Pausa artificial (simula processamento)
    
    pares = []                  # Inicializa lista vazia
    
    # --- Processamento do Loop ---
    for i in l:
        if i % 2 == 0:          # Critério: Verifica se é par
            pares.append(i)     # Ação: Adiciona à lista final
            
    fim = time.time()           # Marca o tempo final (t1)
    
    # Cálculo e exibição do tempo em milissegundos
    tempo_ms = (fim - inicio) * 1000.0
    print(f'Tempo for: {tempo_ms:.0f} ms')
    
    return pares

def numparesL(l):
    """
    Lógica 2: Abordagem Funcional (Pythonic)
    Utiliza filter() e lambda para processar a lista.
    Complexidade: O(n) com overhead de chamadas de função.
    """
    inicio = time.time()        # Marca o tempo inicial
    time.sleep(0.5)             # Pausa artificial
    
    # --- Processamento Funcional ---
    # filter gera o iterador, list materializa os dados na memória
    pares = list(filter(lambda valor: valor % 2 == 0, l))
    
    fim = time.time()           # Marca o tempo final
    
    # Cálculo e exibição do tempo em milissegundos
    tempo_ms = (fim - inicio) * 1000.0
    print(f'Tempo lambda: {tempo_ms:.0f} ms')
    
    return pares

# ============================================================================
#  EXECUÇÃO PRINCIPAL (MAIN)
# ============================================================================

if __name__ == "__main__":
    
    # Configuração dos Dados (Inputs)
    # Inclui teste de estresse com 50 milhões de itens (5*10**7)
    valores = [10**5, 10**6, 5*10**6, 10**7, 5*10**7]

    print("Testando as duas funcoes:")
    print("-" * 50)

    # --- Loop de Testes ---
    for n in valores:
        print(f"\nTestando com {n:,} elementos:")
        print(f"{'='*40}")
        
        # Gera a lista de teste na memória
        lista_range = range(n)

        # 1. Teste com For
        print(f"1. Funcao com for:")
        resultado_for = numpares(lista_range)
        
        # 2. Teste com Lambda
        print(f"2. Funcao com lambda:")
        resultado_lambda = numparesL(lista_range)
        
        # --- Validação dos Resultados ---
        if len(resultado_for) == len(resultado_lambda):
            print(f"[OK] Ambas encontraram {len(resultado_for):,} numeros pares")
        else:
            print("[ERRO] Resultados diferentes!")