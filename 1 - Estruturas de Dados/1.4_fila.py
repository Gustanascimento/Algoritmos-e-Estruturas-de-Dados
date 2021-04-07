# 1.4 - Filas
# Em uma fila o elemento eliminado é sempre o que estava no
# conjunto há mais tempo: a fila implementa uma política do
# primeiro a entrar, primeiro a sair ou FIFO (first-in, first-out).

class Fila:
    def __init__(self):
        self.fila = []

    def imprime(self):
        print(self.fila)

    def tamanho(self):
        return len(self.fila)

    def enqueue(self, elemento):
        self.fila.append(elemento)

    def dequeue(self):
        if (self.tamanho() == 0):
            print("A fila está vazia!")
        else:
            print(f'O cliente {self.fila[0]} foi atendido')
            self.fila.pop(0)

fila = Fila()

x = 10

fila.enqueue(x)
print(f'O cliente {x} foi inserido no fim da fila')

fila.imprime()

fila.dequeue()

fila.imprime()



