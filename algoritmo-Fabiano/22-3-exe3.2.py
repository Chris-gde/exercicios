'''
-mudança 2:
 exibir no final quantas tentativas foram necessárias até acertar
'''
from random import randint
num=randint(1,10)
cont=0
n2=int(input("Digite um numero tentando acertar o primeiro numero: "))
while(n2!=num):
    if n2 < num :
        print("O numero digitado é menor que o primeiro valor")
        n2=int(input("Digite um numero tentando acertar o primeiro numero: "))
        cont=cont+1
    if n2 > num :
        print("O número é maior que o primeiro valor digitado")
        n2=int(input("Digite um numero tentando acertar o primeiro numero: "))
        cont=cont+1
print("Você acertou!!!!")

print("Você errou ", cont)
