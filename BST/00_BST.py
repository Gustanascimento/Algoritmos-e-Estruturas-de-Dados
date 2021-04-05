class No:
    def __init__(self,dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.dado)            

class Arvore_Busca_Binaria:  #Arvore Binaria de Busca Binaria
    def __init__(self,node = None):
        self.nivel=0
        self.raiz = None                
         
    def inserir(self,elemento):    #Insere elemento na arvore
        pai = None
        x = self.raiz
    
        while(x!=None):
            pai = x
            if elemento < x.dado:
                x = x.esquerda
            else:
                x = x.direita              
        if (pai==None):
            self.raiz = No(elemento)
        elif elemento < pai.dado:
            pai.esquerda = No(elemento)
        else:  #elemento>pai.dado
            pai.direita = No(elemento)


    def inserirProf(self,elemento):    #Insere elemento na arvore e imprime em qual profundidade
        pai = None
        x = self.raiz
    
        while(x!=None):
            self.nivel+=1
            pai = x
            if elemento < x.dado:
                x = x.esquerda
            else:
                x = x.direita              
        if (pai==None):
            self.raiz = No(elemento)
        elif elemento < pai.dado:
            pai.esquerda = No(elemento)
        else:
            pai.direita = No(elemento)

        print(self.nivel)                   
        self.nivel=0
        
    def Busca(self, valor):  #Busca se elemento existe na arvore. 
        node=self.raiz       #Caso exista, retorna sua profundidade. Caso nao, retorna -1
            
        while ((self.raiz !=None) and (valor!=node.dado)):
            self.nivel+=1
            if (valor <node.dado):
                node=node.esquerda
                if(node==None):
                    self.nivel=0
                    print("-1")
                    return -1
            else:
                node=node.direita
                if(node==None):
                    self.nivel=0
                    print("-1")
                    return -1
                
        print(self.nivel)
        profundidade=self.nivel
        self.nivel=0
        return profundidade
        

    def Altura(self, node=None):   #Imprime altura da arvore
        if (node==None):
            node = self.raiz
            
        AltEsq=0
        AltDir=0  
        if (node.esquerda != None):
            AltEsq=(self.Altura(node.esquerda))
        if (node.direita != None):
            AltDir=(self.Altura(node.direita))
            
        if (AltDir > AltEsq):
            AltDir+=1
            return AltDir
        else:
            AltEsq+=1
            return AltEsq

    def Minimo(self,valor): #Encontra o minimo
         while(valor.esquerda!=None):
             valor=valor.esquerda
         return valor.dado                

    def remover(self,valor,node="inicio"):

        if (node=="inicio"):
            node=self.raiz            

        if (node.dado==None):
            return node

        if(valor<node.dado):
           node.esquerda=self.remover(valor, node.esquerda)
        elif(valor>node.dado):
            node.direita = self.remover(valor, node.direita)
        else:
            if (node.esquerda==None):
                return node.direita                
            elif(node.direita==None):
                return node.esquerda
            else: 
                substituto=self.Minimo(node.direita)
                node.dado=substituto
                node.direita=self.remover(substituto, node.direita)
        return node

    ######################

    def travessiaPreOrdem(self, node = None):
        if node is None:
            node = self.raiz
        print(node)
        if node.esquerda:
            self.travessiaPreOrdem(node.esquerda)
        if node.direita:
            self.travessiaPreOrdem(node.direita)   


    def travessiaPosOrdem(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.travessiaPosOrdem(node.esquerda)
        if node.direita:
            self.travessiaPosOrdem(node.direita)
        print(node)


    def tavessiaOrdemSimetrica(self, node=None):
        if node is None:
            node = self.raiz
        if node.esquerda:
            self.tavessiaOrdemSimetrica(node.esquerda)
        print(node)
        if node.direita:
            self.tavessiaOrdemSimetrica(node.direita)
            
    #####################


valores=[39, 28, 63, 21, 32, 59, 67, 14, 22, 54, 60, 7, 17]


arvore = Arvore_Busca_Binaria()  #Criacao de um objeto arvore tipo Arvore_Busca_Binaria()

for x in valores:
    arvore.inserir(x) #Insere elementos na árvore


print(arvore.Altura()) #Imprime altura


valor = int(input())
arvore.Busca(valor)  ##Busca valor e retorna profundidade

valor2 = int(input())
arvore.inserir(valor2)  #Insere elemento na árvore

arvore.inserirProf(valor2) #Insere elemento na árvore e exbibe em qual profundidade

valor3 = int(input())
arvore.remover(valor3)  #Remove elemento


arvore.travessiaPreOrdem()

arvore.travessiaPosOrdem()

arvore.tavessiaOrdemSimetrica()

