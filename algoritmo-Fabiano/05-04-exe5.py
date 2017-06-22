'''
6) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''
n=int(input("Informe um numero entre 0 a 10, para gerar a tabuada: "))
cont = 0
print("Tabuada de: ", n)
if n>=1 and n<=10:

 while cont<=10:
  tab = n * cont
  print(n,"x", cont,"=", tab)
  cont = cont + 1

else:
  print("apenas valores de 0 a 10")
