#3.1 - Tabela hash
# O objetivo de hashing é mapear um espaço enorme de
# chaves em um espaço de inteiros relativamente pequeno.

# Isso é feito através de uma função chamada hash function.

# O inteiro gerado pela hash function é chamado hash code
# e é usado para encontrar a localização do item.


class hash_table():
    def __init__(self,maximo):
        self.valorMax = maximo
        self.vetor = [None for x in range(self.valorMax)]

    def __str__(self):
        return str(self.vetor)    

    def get_hash (self, key):
        return key % self.valorMax  #hash function

    def insert (self, key, pessoa):
        h = self.get_hash(key)
        self.vetor[h] = pessoa

    def get_value (self, key):
        h = self.get_hash(key)
        return self.vetor[h]

    def remove (self, key):
        h = self.get_hash(key)
        self.vetor[h] = None



tamanhoMax = int(input())
tabela_Hash = hash_table(tamanhoMax)


index = 1   #hash code
valor = 'Gustavo'

tabela_Hash.insert(index,valor)

valor = tabela_Hash.get_value(1)

print(valor)

print(tabela_Hash)

tabela_Hash.remove(1)

print(tabela_Hash)