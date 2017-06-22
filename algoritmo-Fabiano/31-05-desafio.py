'''
Faça um algoritmo que o usuário informe a quantidade de linhas e colunas que a matriz deve ter.
O sistema deve criar a matriz atribuindo zero para cada campo.
'''
linha=int(input("linhas: "))
colunas=int(input("colunas: "))
m = [0]*linha #ele ta repetindo o 0 a quantidade de vezes de linha q o usuario digitou
for i in range(linha):
    m[i] = [0]*colunas #ele ta repetindo o 0 a quantidade de vezes de colunas q o usuário digitou
print(m)
