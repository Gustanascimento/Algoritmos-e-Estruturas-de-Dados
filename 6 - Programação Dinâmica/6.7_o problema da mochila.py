#6.7 - O problema da mochila 0,1

# O ladrão que assalta uma loja encontra n itens.
# O i-ésimo item vale v[i] reais e pesa w[i].
#   – v[i] e w[i] são inteiros
# Ele deseja levar consigo uma carga mais valiosa possível,
# mas só pode carregar no máximo W quilos em sua mochila,
# sendo W um número inteiro.

# ▪ Que itens ele vai levar?


# Cconsidere que a carga (conjunto de itens) mais valiosa
# pesa no máximo W quilos (que é o que ele suporta).

# Se removermos o item j dessa carga, a carga restante
# deverá ser a carga mais valiosa que pese no máximo W - w[j],
# que o ladrão pode levar dos n-1 itens originais,
# excluindo j.

def mochila(W, wt, val, n):
    grafo = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                grafo[i][w] = 0
            elif wt[i-1] <= w:
                grafo[i][w] = max(val[i-1] + grafo[i-1][w-wt[i-1]],  grafo[i-1][w])
            else:
                grafo[i][w] = grafo[i-1][w]
  
    return grafo[n][W]
  

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print(mochila(W, wt, val, n))
