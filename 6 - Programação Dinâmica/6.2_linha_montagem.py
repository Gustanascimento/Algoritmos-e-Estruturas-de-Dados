#6.2 - Programação de uma linha de montagem

# Suponha que uma indústria possui duas linhas de
# montagem com n estações para fabricar seu produto
# – Cada estação 1 <= j <= n de uma linha i = 1 ou 2 é denotada por S (i,j)
# – Cada estação possui um tempo de montagem distinto (a i,j)

# Para montar um produto, suas peças devem ser transportadas do depósito
# até à linha de montagem:
# – O tempo de transporte de entrada é dado por e

# Da mesma forma, ao ser finalizado, o produto deve ser transportado
# para um armazém
# – O tempo de transporte de cada linha até o armazém é x

# O produto avança de uma estação para outra com tempo desprezível
# - No entanto, se a próxima estação estiver sobrecarregada, o produto
# pode ser deslocado para a estação equivalente na outra linha em tempo t

def linhaMontagem(a, t, e, x,n):
    n = len(a[0])
    T1 = [0 for i in range(n)]
    T2 = [0 for i in range(n)]

    T1[0] = e[0] + a[0][0]
    T2[0] = e[1] + a[1][0]

    linhas = []
    estacoes = []

    if(e[0]<e[1]):
        linhas.append(1)
        estacoes.append(1)
    else:
        linhas.append(2)
        estacoes.append(1)

    for i in range(1, n):
        val1 = T1[i - 1] + a[0][i]
        val2 = T2[i - 1] + t[1][i] + a[0][i]

        if (val1 <val2):
            T1[i] = val1
            linhas.append(2)
        else:
            linhas.append(1)
            T1[i] = val2

        T2[i] = min(T2[i - 1] + a[1][i],
                    T1[i - 1] + t[0][i] + a[1][i])

        estacoes.append(i+1)

    print("Caminho Percorrido:")
    for z in range(len(estacoes)):
       print(f'Linha {linhas[z]} estacao {estacoes[z]}')

    tempo = min(T1[n - 1] + x[0],
               T2[n - 1] + x[1])
    print(f'\nCom um tempo total de {tempo}')


a = [[7, 9, 3, 4, 8, 4],
     [8, 5, 6, 4, 5, 7]]
t = [[0, 2, 3, 1, 3, 4],
     [0, 2, 1, 2, 2, 1]]
e = [2, 4]
x = [3, 2]

n=len(a[0])

linhaMontagem(a, t, e, x,n)


# SAÍDA:
#
# Caminho Percorrido:
# Linha 1 estacao 1
# Linha 2 estacao 2
# Linha 1 estacao 3
# Linha 2 estacao 4
# Linha 2 estacao 5
# Linha 1 estacao 6
#
# Com um tempo total de 38
