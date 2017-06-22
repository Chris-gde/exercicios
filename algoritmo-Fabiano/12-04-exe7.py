'''
7)Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
numeros=[]
cont=0
while cont<10:
  n=int(input("Digite um número: "))
  numeros.append(n)
  cont=cont+1

print(numeros)

numeros.sort(reverse=True) #perguntar ao prof esse codigo ele não só põe em ordem inversa, como tbm põe em ordem do maior pro menor
print(numeros)
