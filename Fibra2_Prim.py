def prim(grafo, quant_V):
    infinito = 9999999

    visitado = quant_V * [False]

    edge = 0
    visitado[0] = True

    comprimento = 0
    while (edge < quant_V - 1):
        minimo = infinito
        x = 0
        y = 0
        for i in range(quant_V):
            if visitado[i]:
                for j in range(quant_V):
                    if ((not visitado[j]) and grafo[i][j]):
                        if minimo > grafo[i][j]:
                            minimo = grafo[i][j]
                            x = i
                            y = j
        comprimento += grafo[x][y]
        visitado[y] = True
        edge += 1

    print(comprimento)


def main():
    lista_bairros = []

    while(True):
        try:
            entrada = input()

            entrada = entrada.split(", ")

            lista_bairros.append((entrada[0],entrada[1],entrada[2]))
        except:
            break

    lista = []
    for bairro in lista_bairros:
        if bairro[0] not in lista:
            lista.append(bairro[0])
        if bairro[1] not in lista:
            lista.append(bairro[1])


    quant_V = len(lista)
    grafo = [[0 for x in range(quant_V)] for y in range(quant_V)]

    for x in lista_bairros:

        if grafo[lista.index(x[0])][lista.index(x[1])]==0.0:
            grafo[lista.index(x[0])][lista.index(x[1])] = int(x[2])
            grafo[lista.index(x[1])][lista.index(x[0])] = int(x[2])

        if(int(x[2]) < grafo[lista.index(x[0])][lista.index(x[1])]):
            grafo[lista.index(x[0])][lista.index(x[1])] = int(x[2])
            grafo[lista.index(x[1])][lista.index(x[0])] = int(x[2])

    prim(grafo,quant_V)

if __name__ == '__main__':
    main()
