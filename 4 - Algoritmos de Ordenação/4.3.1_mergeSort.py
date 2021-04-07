#4.3.1 - Merge Sort
# Dividir o vetor em duas metades
# Ordenar cada uma das metades (aplicar o algoritmo recursivamente)
# Combinar as metades para formar o vetor ordenado

# O algoritmo requer espaço adicional para combinar as metades ordenadas
# Intercalações são feitas em um vetor auxiliar e copiadas de volta para o original

# Nº de comparações -- > Entre N.log(N)/2 e N.log(N) = O(N.log(n))

def merge(vetor, esquerda, direita):
    i = 0
    j = 0
    
    k = 0
    
    while ( j < len(direita) and i < len(esquerda)):
        if esquerda[i] < direita[j]:
            vetor[k] = esquerda[i]
            i+=1
        else:
            vetor[k] = direita[j]
            j+=1
        k+=1

    while (i < len(esquerda)):
        vetor[k] = esquerda[i]
        i+=1
        k+=1

    while (j < len(direita)):
        vetor[k]=direita[j]
        j+=1
        k+=1    

def mergeSort(vetor):
    if len(vetor) > 1:
        meio = len(vetor)//2

        esquerda = vetor[:meio]
        direita = vetor[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        merge(vetor, esquerda, direita)


vetor = [8, 2, 6, 87, 45, 22, 41]

mergeSort(vetor)

print(vetor)
