def main():
    class Pilha:
        def __init__(self):
            self.pilha = []

        def vazio(self):
            if(self.pilha == []):
                return True
            else:
                return False

        def imprime(self):
            return self.pilha

        def push (self, elemento):
            self.pilha.append(elemento)
            
        def pop (self):
            self.pilha.pop()

            
        
    diretorios = Pilha()
    cont=0

    while(1):
        try:
            C=str(input())
            cont+=1
        except EOFError:
            break
        if(len(C)>1024):
            pass
        else:
            if(C=="pwd"):
                string="\\".join(diretorios.imprime())
                print("\\%s"%string)          
                
            else:
                if(cont==1):
                    inicio=C.split("\\")
                    for x in inicio:
                        if x!= '':
                            diretorios.push(x)                    
                else:
                    espaco=C.split(" ")
                    if espaco[1]!="..":
                        lista=espaco[1].split("\\")
                        for x in lista:
                            if x!= '':
                                diretorios.push(x)
                    else:
                        if diretorios.vazio():
                            pass
                        else: 
                            diretorios.pop()             


if __name__ == '__main__':
    main()
