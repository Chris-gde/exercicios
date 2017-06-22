'''

faça um algoritmo uma pessoa informa um número aleatório entre 0 e 10 e outra pessoa irá tentar acertar o numero.
o sistema deve informar se o numero da tentativa é maior ou menor que o numero indicado pelo usuário inicialmente.
o programa só termina quando adivinhar

primeiro usuário informa um numero
segundo usuário entra com um outro numero tentando adivinhar o numero do primeiro usuário

se errar entra num loop e fica nele até acertar
'''

num=int(input("Digite um numero entre 0 a 10: "))
n2=int(input("Digite um numero tentando acertar o primeiro numero: "))
while(n2!=num):
    if n2 < num :
        print("O numero digitado é menor que o primeiro valor")
        n2=int(input("Digite um numero tentando acertar o primeiro numero: "))
    if n2 > num :
        print("O número é maior que o primeiro valor digitado")
        n2=int(input("Digite um numero tentando acertar o primeiro numero: "))
print("Você acertou!!!!")
