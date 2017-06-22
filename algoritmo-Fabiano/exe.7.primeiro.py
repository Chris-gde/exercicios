'''
5)apos calcular o IMC informe, o de acordo com o sexo informe a situação de acordo com a tabela a seguir:

Condição IMC em Mulheres IMC em Homens
abaixo do peso < 19,1 < 20,7
no peso normal 19,1 - 25,8 20,7 - 26,4
marginalmente acima do peso 25,8 - 27,3 26,4 - 27,8
acima do peso ideal 27,3 - 32,3 27,8 - 31,
'''

sexo=input("Digite f caso seu sexo seja feminino ou digite m caso seu sexo seja masculino: ")
peso=int(input("Informe seu peso: "))
altura=float(input("Informe sua altura: "))

# A linguagem tem definido que a utilização de 2 asteriscos seguidos ** significa que o número a esquerda do operador será elevado ao número a direita do operador, por exemplo:
imc= peso/ (altura ** 2)
print("O seu indíce de massa corporal é ", imc)
if sexo == "f":
    if imc < 19.1:
        print("Você está abaixo do peso")
    if imc >= 19.1 and imc < 25.8:
        print("Você está no seu peso normal")
    if imc >= 25.8 and imc < 27.3:
        print("Você está marginalmente acima do seu peso")
    if imc >= 27.3 and imc < 32.3:
        print("Você está acima do seu peso ideal")

if sexo == "m":
    if imc < 20.7:
        print("Você está abaixo do peso")
    if imc >= 20.7 and imc < 26.4:
        print("Você está no seu peso normal")
    if imc >= 26.4 and imc < 27.8:
        print("Você está marginalmente acima do seu peso")
    if imc >= 27.8 and imc < 31:
        print("Você está acima do seu peso ideal")
