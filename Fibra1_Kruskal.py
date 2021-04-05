def kruskal(grafo, quant_V):
    pesos_minimos = []

    grafo = sorted(grafo, key=lambda item: item[2])  #ordenando vertices em ordem decrescente de pesos

    lista_index = []
    rank = []

    for aresta in range(quant_V):
        lista_index.append(aresta)
        rank.append(0)

    index = 0
    edge = 0
    quant_V-=1

    continua = True
    while(continua):
        if(edge < quant_V):

            u ,v , w = grafo[index]

            index = index + 1
            
            x = busca_index(lista_index, u)
            y = busca_index(lista_index, v)

            if x != y:
                edge = edge + 1
                pesos_minimos.append([u, v, w])

                raizesq = busca_index(lista_index, x)
                raizdir = busca_index(lista_index, y)

                if rank[raizesq] < rank[raizdir]:
                    lista_index[raizesq] = raizdir
                elif rank[raizesq] > rank[raizdir]:
                    lista_index[raizdir] = raizesq
                else:
                    lista_index[raizdir] = raizesq
                    rank[raizesq] += 1
            else:
                pass
        else:
            continua = False

    minimo = 0
    for peso in pesos_minimos:
        minimo += peso[2]
    print(minimo)

def busca_index(lista_idx, idx):
    if lista_idx[idx] == idx:
        return idx
    return busca_index(lista_idx, lista_idx[idx])

def main():

    predios = []

    while(True):
        try:
            entrada = input()
            entrada = entrada.split(", ")

            predios.append([entrada[0],entrada[1],int(entrada[2])])
        except:
            break

    lista = []
    for predio in predios:
        if predio[0] not in lista:
            lista.append(predio[0])
        if predio[1] not in lista:
            lista.append(predio[1])

    quant_V = len(lista)

    grafo = []

    for x in predios:
        grafo.append([lista.index(x[0]),lista.index(x[1]),int(x[2])])

    kruskal(grafo, quant_V)

if __name__ == '__main__':
    main()