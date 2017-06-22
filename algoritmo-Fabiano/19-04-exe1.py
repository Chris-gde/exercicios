'''
1)Faça um algoritmo que receba 3 números inteiros e o usuário decida quais das opções o sistema deve retornar:
-a soma dos números
-o maior
-o menor
-a média

n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))
op=int(input("Selecione uma das opções = Soma [1] - Maior [2] - Menor [3] - Media [4]"))
r=(n1+n2+n3)
med=r/3

if n1>n2 and n1>n3:
  M=n1
if n2>n1 and n2>n3:
  M=n2
if n3>n1 and n3>n2:
  M=n3

if n1<n2 and n1<n3:
  m=n1

if n2<n1 and n2<n3:
  m=n2
if n3<n1 and n3<n2:
  m=n3

if op==1:
  print("A soma dos 3 números é: ",r)
if op==2:
  print ("O maior número é: ",M)
if op==3:
  print ("O menor número é: ",m)
if op==4:
  print(" A média é",med)
'''
def lerNumero():
  a=int(input("Digite um número Inteiro: "))
  return(a)

def soma(a,b,c):
  return(a+b+c)

def media(a,b,c):
  return(soma(a,b,c)/3)

def maior(a,b,c):
  if a>b and a>c:
    M=a
  elif b>a and b>c:
    M=b
  elif c>a and c>b:
    M=c
  return (M)

def menor(a,b,c):
  if a<b and a<c:
    M=a
  elif b<a and b<c:
    M=b
  elif c<a and c<b:
    M=c
  return (M)

op=int(input("Selecione uma das opções = Soma [1] - Maior [2] - Menor [3] - Media [4]: "))

n1=lerNumero()
n2=lerNumero()
n3=lerNumero()

if op==1:
  x=soma(n1,n2,n3)
  print("A soma dos 3 números é: ",x)
if op==2:
  x=(maior(n1,n2,n3))
  print ("O maior número é: ",x)
if op==3:
  x=(menor(n1,n2,n3))
  print ("O menor número é: ",x)
if op==4:
  x=(media(n1,n2,n3))
  print(" A média é",x)
