def main():
    class Fila:
        def __init__(self):
            self.fila = []

        def tamanho(self):
            return len(self.fila)
        
        def enqueue(self, musica):
            self.fila.append(musica)

        def dequeue(self):
            self.fila.pop(0)

        def vazia(self):
            if(self.tamanho() == 0):
                return True
            else:
                return False
        
        def play(self):
            if self.vazia():
                print ("...")
            else:
                print(self.fila[0])
                self.dequeue()

        def next(self):
            if self.vazia():
                pass
            else:
                self.dequeue()            
            
        
    spotify = Fila()

    while(1):
        try:
            comando=str(input())
        except EOFError:
            break

        if(len(comando)>100):
            pass

        else:    

            if(comando=="\play"):
                spotify.play()
        
            elif(comando=="\\next"):
                    spotify.next()

            else:
                spotify.enqueue(comando)

if __name__ == '__main__':
    main()
