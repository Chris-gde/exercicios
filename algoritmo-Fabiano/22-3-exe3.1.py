'''
-mudança 1:
o sistema deve gerar o numero aleatório
'''
from random import randint
num=randint(1,10)
n2=int(input("Digite um numero tentando acertar o primeiro numero: "))
while(n2!=num):
    if n2 < num :
        print("O numero digitado é menor que o primeiro valor")
        n2=int(input("Digite um numero tentando acertar o primeiro numero: "))
    if n2 > num :
        print("O número é maior que o primeiro valor digitado")
        n2=int(input("Digite um numero tentando acertar o primeiro numero: ")),
print("Você acertou!!!!")
