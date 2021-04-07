#5.1 - Grafos
# Um grafo é formalmente definido por um par
# – G = (V,E)
# – V é um conjunto de vértices (elementos sendo representados)
# – E é um conjunto de arestas (conexões entre vértices)

# Aplicações: Modelagem de conexões entre pares de  elementos
# Exemplos:
#   Navegação: Conhecer a rota mais curta entre dois pontos da cidade?
#   Web: Páginas contêm links para outras páginas.
#   Circuitos elétricos: Desenho do circuito integrado
#   Agendamento de tarefas: Um processo para ser executado depende de várias tarefas não independentes entre si. Em que ordem as tarefas devem ser executadas?
#   Redes de computadores: Entender a estrutura da rede para dimensionar a infraestrutura, encontrar pontos críticos da rede
#   Atribuição de pessoas a cargos
#   Redes sociais: Pessoas seguem amigos. Descobrir grupos de pessoas com interesses em comum.


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


#Início#


D = 'NAO DIRECIONADO'       #direcao
#D = 'DIRECIONADO'

vertices = [(0, 2), (0, 5), (0, 4), (2, 3), (1, 3), (3, 5)] 

valores = []  #Conta a quantidade de valores sem repetição
aux = 0
for x in vertices:
    for i in x:
        if(int(i) not in valores):
            valores.append(int(i))
            if(int(i))>aux:
                aux=int(i)
aux+=1

print(f'(Total de {aux} valores, os quais são:{valores})')

grafo = [[] for y in range(aux)]

if(D=='NAO DIRECIONADO'):
    for x in vertices:
        grafo[x[0]].append(x[1])
        grafo[x[1]].append(x[0])

elif(D=='DIRECIONADO'):
    for y in vertices:
        grafo[y[0]].append(y[1])

#print("Grafo",grafo)

print("\nBusca em profundidade: ")
buscaProfundidade(grafo,aux)

print("\nBusca em largura: ")
buscaLargura(grafo,aux)
