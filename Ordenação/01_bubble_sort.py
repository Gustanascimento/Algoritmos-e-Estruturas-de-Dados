def bubbleSort(vetor): 
    N = len(vetor)
    
    for i in range(N): 
        for j in range(0, N-i-1): 
            if vetor[j] > vetor[j+1] : 
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j] 
  
vetor = [8, 2, 6, 87, 45, 22, 41]
  
bubbleSort(vetor)

print(vetor)