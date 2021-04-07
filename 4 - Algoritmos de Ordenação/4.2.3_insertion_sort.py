#4.2.3 - Insertion Sort
# Dividir vetor entre ordenados (à esquerda) e a ordenar (à direita)
# Inserir primeiro elemento da direita na subsequência ordenada da esquerda
# Repetir processo até que todos tenham sido avaliados

# Melhor caso (Elemento encontra-se na posição correta, 1 única comparação): 
# Nº de comparações -- > C(N) = O(n)
# Nº de trocas (movimentações) --> M(N) = O(n)

# Pior caso: 
# Nº de comparações -- > C(N) = O(n²)
# Nº de trocas (movimentações) --> M(N) = O(n²)


def insertionSort(vetor):
    N = len(vetor)

    for i in range(1,N): 
  
        aux = vetor[i] 

        j = i-1

        while j >= 0 and vetor[j] > aux: 
                vetor[j + 1] = vetor[j] 
                j -= 1
        vetor[j + 1] = aux 

vetor = [8, 2, 6, 87, 45, 22, 41] 

insertionSort(vetor) 

print(vetor)
