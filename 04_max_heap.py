def max_heapify(heap, index): 
    maior = index  #insere valor da metade do vetor como raiz (pois eh o maior)
    
    tamanho = len(heap)

    esquerda = 2 * index + 1  
    direita = 2 * index + 2 

    if esquerda < tamanho and heap[esquerda] > heap[maior]: 
        maior = esquerda  
    if direita < tamanho and heap[direita] > heap[maior]: 
        maior = direita    
    
    if heap[maior] > heap[index]: 
        heap[index], heap[maior] = heap[maior], heap[index]
        max_heapify(heap, maior)  

def build_max_heap(vetor):
    metade = len(vetor)//2

    while (metade>=0):
        max_heapify(vetor,metade)
        metade-=1
    return vetor


vetor = [5,6,8,3,7,9]

build_max_heap(vetor)

print(vetor)