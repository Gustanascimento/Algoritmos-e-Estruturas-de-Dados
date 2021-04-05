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