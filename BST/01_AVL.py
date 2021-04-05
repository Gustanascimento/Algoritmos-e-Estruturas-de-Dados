class Node(): 
    def __init__(self, val): 
        self.val = val 
        self.esquerda = None
        self.direita = None
        self.height = 1
  
class Arvore_AVL(): 
    def insert(self, raiz, valor):
        if not raiz: 
            return Node(valor) 
        elif valor < raiz.val: 
            raiz.esquerda = self.insert(raiz.esquerda, valor) 
        else: 
            raiz.direita = self.insert(raiz.direita, valor) 
  
        raiz.height = 1 + max(self.getHeight(raiz.esquerda), 
                          self.getHeight(raiz.direita)) 
  
        balance = self.getBalance(raiz)
        
        if balance > 1 and valor < raiz.esquerda.val: 
            return self.direitaRotate(raiz) 
        if balance < -1 and valor > raiz.direita.val: 
            return self.esquerdaRotate(raiz) 
        if balance > 1 and valor > raiz.esquerda.val: 
            raiz.esquerda = self.esquerdaRotate(raiz.esquerda) 
            return self.direitaRotate(raiz) 
        if balance < -1 and valor < raiz.direita.val: 
            raiz.direita = self.direitaRotate(raiz.direita) 
            return self.esquerdaRotate(raiz) 
        return raiz 

    def delete(self, raiz, valor): 

        if not raiz: 
            return raiz 
  
        elif valor < raiz.val: 
            raiz.esquerda = self.delete(raiz.esquerda, valor) 
  
        elif valor > raiz.val: 
            raiz.direita = self.delete(raiz.direita, valor) 
  
        else: 
            if raiz.esquerda is None: 
                temp = raiz.direita 
                raiz = None
                return temp 
  
            elif raiz.direita is None: 
                temp = raiz.esquerda 
                raiz = None
                return temp 
  
            temp = self.getMinValueNode(raiz.direita) 
            raiz.val = temp.val 
            raiz.direita = self.delete(raiz.direita, 
                                      temp.val) 
  
        if raiz is None: 
            return raiz
        
        raiz.height = 1 + max(self.getHeight(raiz.esquerda), 
                            self.getHeight(raiz.direita)) 
        balance = self.getBalance(raiz) 
  
        if balance > 1 and self.getBalance(raiz.esquerda) >= 0: 
            return self.direitaRotate(raiz) 
  
        if balance < -1 and self.getBalance(raiz.direita) <= 0: 
            return self.esquerdaRotate(raiz) 
  
        if balance > 1 and self.getBalance(raiz.esquerda) < 0: 
            raiz.esquerda = self.esquerdaRotate(raiz.esquerda) 
            return self.direitaRotate(raiz) 
  
        if balance < -1 and self.getBalance(raiz.direita) > 0: 
            raiz.direita = self.direitaRotate(raiz.direita) 
            return self.esquerdaRotate(raiz) 
  
        return raiz 
  
    def esquerdaRotate(self, z): 
  
        y = z.direita 
        T2 = y.esquerda 
  
        y.esquerda = z 
        z.direita = T2 
  
        z.height = 1 + max(self.getHeight(z.esquerda),  
                         self.getHeight(z.direita)) 
        y.height = 1 + max(self.getHeight(y.esquerda),  
                         self.getHeight(y.direita))   
        return y 
  
    def direitaRotate(self, z): 
  
        y = z.esquerda 
        T3 = y.direita 
  
        y.direita = z 
        z.esquerda = T3 

        z.height = 1 + max(self.getHeight(z.esquerda), 
                          self.getHeight(z.direita)) 
        y.height = 1 + max(self.getHeight(y.esquerda), 
                          self.getHeight(y.direita)) 
        return y 
  
    def getHeight(self, raiz): 
        if not raiz: 
            return 0
        return raiz.height 
  
    def getBalance(self, raiz): 
        if not raiz: 
            return 0
        return self.getHeight(raiz.esquerda) - self.getHeight(raiz.direita) 
  
    def getMinValueNode(self, raiz): 
        if raiz is None or raiz.esquerda is None: 
            return raiz 
  
        return self.getMinValueNode(raiz.esquerda) 
  
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
    raiz = Arvore.insert(raiz, x) 
  
# preOrdem Traversal 
print("preOrdem Traversal after insertion -") 
Arvore.preOrdem(raiz) 
print() 
  
# Delete 
valor = 10
raiz = Arvore.delete(raiz, valor) 
  
# preOrdem Traversal 
print("preOrdem Traversal after deletion -") 
Arvore.preOrdem(raiz) 
print() 
