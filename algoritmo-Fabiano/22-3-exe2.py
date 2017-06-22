'''
2) Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo, e caso seja um quadrado, exibir a frase: área de um quadrado

ler base e altura

'''

base=int(input("Digite a base: "))
altura=int(input("Digite a altura: "))

retangulo= base * altura
if base == altura :
    print("Área de um quadrado")
else:
    print("A área do retangulo é: ", retangulo)
