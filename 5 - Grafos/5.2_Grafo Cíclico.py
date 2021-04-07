#5.2 - Algoritmo que verifica se um grafo possui ciclos

class grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[] for x in range(vertices)]

    def inserirNaoDirecionado(self, v, w):
        self.grafo[v].append(w)
        self.grafo[w].append(v)

    def dfs(self, v, marcado, antecessor):

        marcado[v] = True

        for i in self.grafo[v]:
            if marcado[i] == False:
                valor3 = self.dfs(i, marcado, v)
                if (valor3 == True):
                    return True
            elif (antecessor != i):
                return True
        return False

    def buscaProfundidade(self):
        marcado = [False] * (self.V)
        for i in range(self.V):
            if marcado[i] == False:
                valor2 = (self.dfs(i, marcado, -1))
                if (valor2 == True):
                    return True
        return False



vertices = [(0, 2), (0, 5), (0, 4), (2, 3), (1, 3), (3, 5)] 


valores = []
aux = 0
for x in vertices:
    if(int(x[0]) not in valores):
        valores.append(int(x[0]))
        if(int(x[0]))>aux:
            aux=int(x[0])
    if(int(x[1]) not in valores):
        valores.append(int(x[1]))
        if(int(x[1]))>aux:
            aux=int(x[1])
aux+=1

g = grafo(aux)

for x in vertices:
    g.inserirNaoDirecionado(x[0],x[1])

valor = g.buscaProfundidade()

if (valor==True):
    print("Grafo contem ciclo")
else:
    print("Grafo nao contem ciclo")
