'''
5) Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''
n1=int(input("Digite o primeiro número, ele deverá ser menor que o segundo número: "))
n2=int(input("Digite o segundo número, ele deverá ser maior que o primeiro número: "))

for i in range(n1+1,n2):
  print(i)
