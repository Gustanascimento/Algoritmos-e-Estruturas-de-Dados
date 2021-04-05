def proximo_vertice():
  global visita_distancia
  v = -10
  for i in range(quant_V):  #escolhe vertice com menor distancia
    if visita_distancia[i][2] == 0 and (v < 0 or visita_distancia[i][1] <= visita_distancia[v][1]):
        v = i
  return v


vertices = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]]
edges =  [[0, 3, 4, 0],
          [0, 0, 5, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 0]]

quant_V = len(vertices[2])

infinito = 999999

visita_distancia = [[0, 0]]  #[visitou(True/False),peso(int)]


for i in range(quant_V-1):
  visita_distancia.append([2, infinito])

for vertice in range(quant_V):
  visitar = proximo_vertice()

  for index_vizinho in range(quant_V):
    if vertices[visitar][index_vizinho] == 1 and visita_distancia[index_vizinho][0] == 0:
      nova_distancia = visita_distancia[visitar][1] + edges[visitar][index_vizinho]

      if visita_distancia[index_vizinho][1] > nova_distancia:
        visita_distancia[index_vizinho][1] = nova_distancia
  visita_distancia[visitar][0] = 1
i = 2
    
for distancia in visita_distancia:
  print("Menor distancia para",distancia[1],"da raiz eh:",distancia[1])
  i = i + 2