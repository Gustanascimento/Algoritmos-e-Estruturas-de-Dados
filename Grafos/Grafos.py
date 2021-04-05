def buscaLargura(grafo,quant_V):
    marcado = quant_V * [False] 
    antecessor = quant_V * [-1]
    vertices = []

    for i in range(quant_V):
        if (marcado[i]!=True):
            marcado[i]=True
            vertices.append(i)

            while(len(vertices)>0):
                v = vertices.pop(0)

                for u in grafo[v]:
                    if (marcado[u]==False):
                        marcado[u]=True
                        vertices.append(u)
                        antecessor[u]=v
    print(antecessor)
    del marcado
    del antecessor

def dfs(grafo, vertice, marcado, antecessor):
    marcado[vertice] = True

    for i in grafo[vertice]:
        if (marcado[i]==False):
            antecessor[i] = vertice
            dfs(grafo, i, marcado, antecessor)

def buscaProfundidade(grafo,quant_V):
    marcado = quant_V * [False] 
    antecessor = quant_V * [-1]

    for v in range(quant_V):
        if(marcado[v]==False):
            dfs(grafo,v,marcado,antecessor)

    print(antecessor)
    del marcado
    del antecessor

def main():
    D = input()       #direcao
    V = input()       #vertices

    V = V.split(" ")

    vertices=[]  #arestas

    for x in V:
        y = tuple(eval(x))
        vertices.append(y)


    valores = []
    aux = 0
    for x in vertices:
        for i in x:
            if(int(i) not in valores):
                valores.append(int(i))
                if(int(i))>aux:
                    aux=int(i)
    aux+=1
    
    grafo = [[] for y in range(aux)]

    if(D=='NAO DIRECIONADO'):
        for x in vertices:
            grafo[x[0]].append(x[1])
            grafo[x[1]].append(x[0])

    elif(D=='DIRECIONADO'):
        for y in vertices:
            grafo[y[0]].append(y[1])

   #print(grafo)

    buscaProfundidade(grafo,aux)
    buscaLargura(grafo,aux)

if __name__ == '__main__':
    main()
