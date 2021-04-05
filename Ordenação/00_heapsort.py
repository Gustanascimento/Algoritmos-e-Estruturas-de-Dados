def max_heapify(vetor, n, index): 
    maior = index
    esquerda = 2 * index + 1    
    direita = 2 * index + 2     

    if esquerda < n and vetor[index] < vetor[esquerda]: 
        maior = esquerda 
    if direita < n and vetor[maior] < vetor[direita]: 
        maior = direita 

    if maior != index:
        vetor[index],vetor[maior] = vetor[maior],vetor[index] 
        max_heapify(vetor, n, maior) 
  
def heapSort(vetor): 
    N = len(vetor) 
  
    for x in range(N//2 - 1, -1, -1): 
        max_heapify(vetor, N, x) 

    for y in range(N-1, 0, -1): 
        vetor[y], vetor[0] = vetor[0], vetor[y]
        max_heapify(vetor, y, 0) 
  

vetor = [12, 11, 13, 5, 6, 7] 

heapSort(vetor)

print (vetor)