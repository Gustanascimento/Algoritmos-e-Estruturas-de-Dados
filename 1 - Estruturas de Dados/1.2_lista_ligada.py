#1.2 - Listas Ligadas
# Estrutura de dados linear e dinâmica composta por várias células que estão interligadas
# através de ponteiros, ou seja, cada célula possui um ponteiro que aponta para o endereço
# de memória da próxima célula.

# Para uma visualização gráfica da lista ligada e facilitar o entendimento,
# colocar o código abaixo no Python Tutor: http://pythontutor.com/live.html#mode=edit

class ListaLigada:
  def __init__(self, chave):
    self.noEsquerda = None
    self.noDireita = None
    self.chave = chave

def inserirElemento(listaLigada, chaveNovoNo):
  novoNo = ListaLigada(chaveNovoNo)
  if (listaLigada == None):
    listaLigada = novoNo
  else:
    noTemp = listaLigada
    listaLigada = novoNo
    listaLigada.noDireita = noTemp
    if (noTemp != None):
      noTemp.noEsquerda = novoNo
  return listaLigada

def removerElemento(listaLigada):
  while (listaLigada.noDireita!=None):
    listaLigada = listaLigada.noDireita 
  novaLista = listaLigada.noEsquerda
  novaLista.noDireita = None
  listaLigada.noEsquerda = None
  return novaLista

def imprimirElementos(listaLigada):
  while (listaLigada.noDireita!=None):
    listaLigada = listaLigada.noDireita    
  noBusca = listaLigada
  
  while (noBusca != None):
    print(noBusca.chave)
    noBusca = noBusca.noEsquerda
  return noBusca

listaLigada = None
listaLigada = inserirElemento(listaLigada, 4)
listaLigada = inserirElemento(listaLigada, 2)
listaLigada = inserirElemento(listaLigada, 6)
listaLigada = inserirElemento(listaLigada, 10)
listaLigada = inserirElemento(listaLigada, 16)

imprimirElementos(listaLigada)
print("")
listaLigada = removerElemento(listaLigada)
imprimirElementos(listaLigada)
print("")
listaLigada = removerElemento(listaLigada)
imprimirElementos(listaLigada)
print("")
listaLigada = removerElemento(listaLigada)
imprimirElementos(listaLigada)
print("")
listaLigada = removerElemento(listaLigada)
imprimirElementos(listaLigada)
