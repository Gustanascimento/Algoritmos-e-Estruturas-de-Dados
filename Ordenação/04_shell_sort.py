def shellSort(vetor): 
    N = len(vetor)
    h = 1
    
    while h < N//3:
        h = 3*h+1
  
    while h >= 1: 
        for i in range(h, N): 
            v_temp = vetor[i] 
            j = i 

            while  j >= h and vetor[j-h] > v_temp: 
                vetor[j] = vetor[j-h] 
                j -= h 
            vetor[j] = v_temp 
        h //= 3

vetor = [8, 2, 6, 87, 45, 22, 41]

shellSort(vetor)

print(vetor)