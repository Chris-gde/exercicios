'''
3) Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:
infantil A = 5 - 7 anos
infantil B = 8 -10 anos
juvenil A = 11 -13 anos
juvenil B = 14 -17 anos
adulto = maiores de 18 anos

usuario vai informar a idade:

se idade for

'''
idade=int(input("Informe sua idade: "))

if idade >= 5 and idade <= 7:
    print("Sua categoria é Infantil A")
if idade >= 8 and idade <= 10:
    print("Sua categoria é Infantil B")
if idade >= 11 and idade <= 13:
    print("Sua categoria é Juvenil A")
if idade >= 14 and idade <= 17:
    print("Sua categoria é Juvenil B")
if idade >= 18:
    print("Sua categoria é Adulto")
