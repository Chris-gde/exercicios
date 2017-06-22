'''
1) Faça um algoritmo que leia a data de nascimento de uma pessoa e mostre-a expressa em anos, meses e dias.

'''

dias=int(input("Digite o Dia que você nasceu: "))
meses=int(input("Digite o Mês que você nasceu: "))
anos=int(input("Digite o Ano que você nasceu: "))
print("Você nasceu em:", dias,"/",meses,"/",anos)
idade=2017 - anos
print("A sua idade é:", idade)
m=idade * 12
print("A quantidade de Mesês são:", m)
d=dias + (meses * 30) + (idade * 365)
print("A quantidade de Dias são:", d)

