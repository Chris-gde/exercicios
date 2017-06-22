'''
4) Faça um algoritmo para efetuar o cálculo do IMC. Sabendo que é feito dividindo o peso (em quilogramas) pela altura (em metros) ao quadrado.

imc=peso/altura ao quadrado
'''
peso=int(input("Informe seu peso: "))
altura=float(input("Informe sua altura: "))

# A linguagem tem definido que a utilização de 2 asteriscos seguidos ** significa que o número a esquerda do operador será elevado ao número a direita do operador, por exemplo:
imc= peso/ (altura ** 2)

print("O seu indíce de massa corporal é ", imc)
