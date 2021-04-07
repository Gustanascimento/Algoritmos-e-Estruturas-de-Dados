#4.3.2 - Quicksort
# Vetor é particionado em dois subvetores conforme um pivô
    # Elementos à esquerda do pivô são menores que ele
    # Elementos à direita do pivô são maiores que ele
# O algoritmo é aplicado a cada um dos subvetores e, ao terminar, o vetor encontra-se ordenado

# Dependendo da escolha do pivô, partição pode ficar desbalanceada

# Nº de comparações -- > Entre O(N.log(n)) no melhor caso e O(N²) no pior caso
# Para evitar o pior caso, escolhe-se um pivô aleatório


#Implementação original (o pivô é o primeiro elemento):
def particao(array, esquerda, direita):
    pivo = array[esquerda]
    print(pivo)
    i = esquerda + 1
    j = direita

    while (1):
        while i <= j and array[j] >= pivo:
            j-=1

        while i <= j and array[i] <= pivo:
            i+=1

        if i >= j:
            break    
        else:
            array[i], array[j] = array[j], array[i]
    array[esquerda], array[j] = array[j], array[esquerda]

    print("arr",array)
    return j 

def qs(v, esquerda, direita):
    if esquerda>=direita:
        return
    part = particao(v, esquerda, direita)
    qs(v, esquerda, part-1)
    qs(v, part+1, direita)

def quickSort(vetor):
    qs (vetor, 0, len(vetor)-1)

vetor = [90, 40, 20, 30, 10, 2, 3, 6, 100, 65, 12, 56, 13, 577, 1]

quickSort(vetor)

print(vetor)

