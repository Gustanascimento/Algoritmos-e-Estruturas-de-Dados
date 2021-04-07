#5.3_Djisktra
# Algoritmo que busca encontrar o caminho mais curto
# (com o menor custo) entre dois vértices

# Associaremos ao conjunto de vértices um vetor p que
# armazenará uma estimativa de menor caminho entre s e os
# demais vértices

# Relaxamento: Caso exista um caminho mais curto até v
# passando por u, então o antecessor de v é atualizado,
# assim como seu custo

# O algoritmo mantém um vetor de antecessores a e de pesos
# estimados p os quais são inicializados com -1 e infinito
# (exceto p[0] = 0), onde 0 é o no raiz, fonte ou source.

def dijkstra(grafo, origem, destino, V):
    p = [999999] * V
    p[origem] = 0
    marcador = [-1] * V
    fila = []
    
    for k in range(V):
        fila.append(k)
        
    for j in range(V):

        menor = 999999
        for v in range(V):
            if p[v] < menor and v in fila:
                menor = p[v]
                u = v
        try:
            fila.remove(u)
        except:
            pass

        relaxar(grafo, u, V, p, marcador, fila)

    caminho(marcador, destino)

    return p[destino]

def relaxar(grafo, u, V, p, marcador, fila):
    for v in range(V):
        
        if grafo[u][v] and v in fila : 
            if p[v] > p[u] + grafo[u][v]: 
                p[v] = p[u] + grafo[u][v]
                marcador[v] = u

def caminho(parent, j):
    global conexoes
    if parent[j] == -1 :  
        conexoes.append(j)
        return
    conexoes.append(j)
    caminho(parent , parent[j])

def mostrar_rota(lista):
    string = "Rota: "
    for c in reversed(lista):
        string += str(c)
        string += " --> "

    string = string[:-4]
    print(string)

grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

v = len(grafo)

origem = int(input())
destino = int(input())

conexoes = []
distancia = dijkstra(grafo, origem, destino, v)

print("\nO menor caminho entre", origem,"e",destino,"tem", distancia,"km")

mostrar_rota(conexoes)


#Respostas esperadas:
#O menor caminho entre 0 e 0 tem 0 km
#Rota: 0
#O menor caminho entre 0 e 1 tem 4 km
#Rota: 0 --> 1
#O menor caminho entre 0 e 7 tem 8 km
#Rota: 0 --> 7
#...



