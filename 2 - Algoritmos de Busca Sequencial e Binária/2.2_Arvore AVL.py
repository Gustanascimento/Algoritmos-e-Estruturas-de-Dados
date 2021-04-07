#2.2 - Árvore AVL
# As árvores AVL foram ropostas em 1962 pelos matemáticos russos
# G.M. (A)delson-(V)elskki e E.M. (L)andis. O diferencial são seus
# métodos de inserção e remoção de elementos da árvore de forma
# que ela fique sempre balanceada. 

# PROPRIEDADE AVL:
# Para todo nó: |altura(direita) - altura(esq)| < 2

# Applet para visualização de árvores AVL:
# https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

class No(): 
    def __init__(self, val): 
        self.val = val 
        self.esquerda = None
        self.direita = None
        self.altura = 1
  
class Arvore_AVL(): 
    def inserir(self, raiz, valor):
        if not raiz: 
            return No(valor) 
        elif valor < raiz.val: 
            raiz.esquerda = self.inserir(raiz.esquerda, valor) 
        else: 
            raiz.direita = self.inserir(raiz.direita, valor) 
  
        raiz.altura = 1 + max(self.getAltura(raiz.esquerda), 
                          self.getAltura(raiz.direita)) 
  
        balanco = self.balanceamento(raiz)
        
        if balanco > 1 and valor < raiz.esquerda.val: 
            return self.rotacionaDireita(raiz) 
        if balanco < -1 and valor > raiz.direita.val: 
            return self.rotacionaEsquerda(raiz) 
        if balanco > 1 and valor > raiz.esquerda.val: 
            raiz.esquerda = self.rotacionaEsquerda(raiz.esquerda) 
            return self.rotacionaDireita(raiz) 
        if balanco < -1 and valor < raiz.direita.val: 
            raiz.direita = self.rotacionaDireita(raiz.direita) 
            return self.rotacionaEsquerda(raiz) 
        return raiz 

    def remover(self, raiz, valor): 

        if not raiz: 
            return raiz 
  
        elif valor < raiz.val: 
            raiz.esquerda = self.remover(raiz.esquerda, valor) 
  
        elif valor > raiz.val: 
            raiz.direita = self.remover(raiz.direita, valor) 
  
        else: 
            if raiz.esquerda is None: 
                temp = raiz.direita 
                raiz = None
                return temp 
  
            elif raiz.direita is None: 
                temp = raiz.esquerda 
                raiz = None
                return temp 
  
            temp = self.getMinimo(raiz.direita) 
            raiz.val = temp.val 
            raiz.direita = self.remover(raiz.direita, 
                                      temp.val) 
  
        if raiz is None: 
            return raiz
        
        raiz.altura = 1 + max(self.getAltura(raiz.esquerda), 
                            self.getAltura(raiz.direita)) 
        balanco = self.balanceamento(raiz) 
  
        if balanco > 1 and self.balanceamento(raiz.esquerda) >= 0: 
            return self.rotacionaDireita(raiz) 
  
        if balanco < -1 and self.balanceamento(raiz.direita) <= 0: 
            return self.rotacionaEsquerda(raiz) 
  
        if balanco > 1 and self.balanceamento(raiz.esquerda) < 0: 
            raiz.esquerda = self.rotacionaEsquerda(raiz.esquerda) 
            return self.rotacionaDireita(raiz) 
  
        if balanco < -1 and self.balanceamento(raiz.direita) > 0: 
            raiz.direita = self.rotacionaDireita(raiz.direita) 
            return self.rotacionaEsquerda(raiz) 
  
        return raiz 
  
    def rotacionaEsquerda(self, z): 
  
        y = z.direita 
        T2 = y.esquerda 
  
        y.esquerda = z 
        z.direita = T2 
  
        z.altura = 1 + max(self.getAltura(z.esquerda),  
                         self.getAltura(z.direita)) 
        y.altura = 1 + max(self.getAltura(y.esquerda),  
                         self.getAltura(y.direita))   
        return y 
  
    def rotacionaDireita(self, z): 
  
        y = z.esquerda 
        T3 = y.direita 
  
        y.direita = z 
        z.esquerda = T3 

        z.altura = 1 + max(self.getAltura(z.esquerda), 
                          self.getAltura(z.direita)) 
        y.altura = 1 + max(self.getAltura(y.esquerda), 
                          self.getAltura(y.direita)) 
        return y 
  
    def getAltura(self, raiz): 
        if not raiz: 
            return 0
        return raiz.altura 
  
    def balanceamento(self, raiz): 
        if not raiz: 
            return 0
        return self.getAltura(raiz.esquerda) - self.getAltura(raiz.direita) 
  
    def getMinimo(self, raiz): 
        if raiz is None or raiz.esquerda is None: 
            return raiz 
  
        return self.getMinimo(raiz.esquerda) 
  
    def preOrdem(self, raiz):  
        if not raiz: 
            return
        print(raiz.val) 
        self.preOrdem(raiz.esquerda) 
        self.preOrdem(raiz.direita) 
  

Arvore = Arvore_AVL() 
raiz = None
valores = [9, 5, 10, 0, 6, 11, -1, 1, 2] 
  
for x in valores: 
    raiz = Arvore.inserir(raiz, x) 
  
print("Travessia em pre ordem antes da inserção:") 
Arvore.preOrdem(raiz) 

  
# Deletar 
raiz = Arvore.remover(raiz, 10) 
  
# preOrdem Traversal 
print("\nTravessia pre ordem apos remover elemento 10:") 
Arvore.preOrdem(raiz)
