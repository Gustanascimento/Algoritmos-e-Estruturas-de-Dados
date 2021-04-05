def qs(v, esq, dir):
    if esq >= dir:
        return
    p = particao(v,esq,dir)
    qs(v,esq,p-1)
    qs(v,p+1,dir)

def quicksort(v, N):
    x = v[0]
    vetor[0]= vetor[4]  # <--- Colocar aqui o index do elemento da lista a ser 
    vetor[1] = x        ###### utilizado como pivô inicial
    qs(v, 0, N-1)


def particao(v, esq, dir):
    
    pivo = v[esq]; i = esq; j = dir+1
    print(f'pivo {pivo}')

    while(True):
        i+=1
        while v[i] < pivo:
            if i >= dir: break
            i+=1
        j-=1
        while v[j] > pivo:
            if j <= esq: break
            j-=1
        if i >= j : break
        trocar(v,i,j)
    trocar(v,esq,j)
    print(vetor)
    return j


def trocar(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp


vetor = [90,40,20,30,10,2,3,6,100,65,12,56,13,577,1]

print(vetor)
quicksort(vetor, 15)

print(vetor)
