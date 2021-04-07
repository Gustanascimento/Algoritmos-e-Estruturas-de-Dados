#4.2.1 - Bubble Sort
# Repetidas trocas entre elementos consecutivos
# Se o elemento for maior que o próximo: Trocar
# Elementos maiores "flutuam" em direção ao fim do vetor

# Nº de comparações -- > C(N) = O(n²)
# Nº de trocas (movimentações) --> M(N) = O(n²) no pior caso

# Péssimo desempenho
# Estável
# Custo independe se vetor está parcialmente ordenado
# Fácil Implementação; pouco utilizado

def bubbleSort(vetor): 
    N = len(vetor)
    
    for i in range(N): 
        for j in range(0, N-i-1): 
            if vetor[j] > vetor[j+1] : 
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j] 
  
vetor = [8, 2, 6, 87, 45, 22, 41]
  
bubbleSort(vetor)

print(vetor)
