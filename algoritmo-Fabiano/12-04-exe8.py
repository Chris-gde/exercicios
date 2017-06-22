'''
8) Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''
pares = 0
impares = 0
vetorPar=[]
vetorImpar=[]
vetor=[]
for i in range(0, 20):
  numero = int(input('Informe um numero: '))
  if (numero % 2 == 0):
    vetorPar.append(numero)
    vetor.append(numero)
    pares += 1
  else:
    vetorImpar.append(numero)
    vetor.append(numero)
    impares += 1

print ('Vetor com todos os números ', vetor)
print ('Vetor de números pares: ', vetorPar)
print ('Vetor de números impares: ', vetorImpar)
