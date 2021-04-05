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