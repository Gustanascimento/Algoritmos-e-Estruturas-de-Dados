# 1.3 - Pilhas
# Em uma pilha, o elemento eliminado do conjunto é o
# mais recentemente inserido: a pilha implementa uma
# política de último a entrar, primeiro a sair ou LIFO
# (last-in, first-out)

class Pilha:
    def __init__(self):
        self.pilha = []

    def imprime(self):
        print(self.pilha)
        
    def tamanho(self):
        print(len(self.pilha))

    def push (self, elemento):
        self.pilha.append(elemento)

    def pop (self):
        if (self.pilha == []):
            print("A pilha está vazia!")
        else:
            self.pilha.pop()

pilha = Pilha()

x = 10

pilha.push(x)
print(f'O elemento {x} foi inserido no topo da pilha')

pilha.imprime()

pilha.pop() #Remove elemento do topo da pilha
print(f'O elemento do topo foi removido')
