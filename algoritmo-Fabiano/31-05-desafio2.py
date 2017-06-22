'''
Faça um programa onde o usuário informe a km inicial no momento que o tanque é cheio, no próximo abastecimento
o usuário deve informar os km percorridos e a quantidade de combustível necessária para completar o tanque (l).
O sistema deve informar a o consumo médio (km/l).
'''
n=int(input("Informe a kilometragem inicial: "))
percorrido=int(input("Informe os kilometros percorridos: "))
litros=int(input("Informe a quantidade de combustivel necessária para completar o tanque: "))

km=percorrido-n
consumo=km/litros

print("Seu consumo médio foi: ",consumo)
