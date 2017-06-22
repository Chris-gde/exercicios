'''
(2) - A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
'''
termo = 0
while (termo <= 0):
  termo = int(input('Voce quer que a serie de Fibonacci vá ate qual termo? '))
  if (termo <= 0):
    print('O termo deve ser positivo!')


f1 = 1
print (f1)
f2 = 1
for i in range(1, termo):
  print(f2)
  f3 = f1 + f2
  f1 = f2
  f2 = f3

