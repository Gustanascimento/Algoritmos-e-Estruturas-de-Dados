#4.2.2 - Selection Sort
# Encontrar o menor elemento do vetor
# Trocá-lo com o primeiro elemento
# Desconsiderar menor elemento
# Repetir processo para os demais

# Nº de comparações -- > C(N) = O(n²)
# Nº de trocas (movimentações) --> M(N) = O(n)

# Poucas trocas = Útil p/ casos em que os itens são grandes
# Não estável!
# Custo independe se vetor está parcialmente ordenado
# Fácil Implementação


def selection_sort(vetor):
    N = len(vetor)
    for i in range(N): 
        minimo = i 
        for j in range(i+1, N): 
            if vetor[minimo] > vetor[j]: 
                minimo = j       
        vetor[i], vetor[minimo] = vetor[minimo], vetor[i] 

vetor = [8, 2, 6, 87, 45, 22, 41] 

selection_sort(vetor)

print(vetor)
