'''
4)sistema deve perguntar quantos cigarros a pessoa fuma por dia e por quantos anos ela já fuma. Sabendo que cada cigarro se perde 10min de vida sistema deve calcular quantos dias de vida o fumante perderá

1 cigarro perde-se 10 min
'''
cigarro=int(input("Digite quantos cigarros você fuma por dia: "))
ano=int(input("Digite por quantos anos você já fuma: "))

totalCigarros = (ano * 365)*cigarro
diasPerdidos = (totalCigarros * 10)/24

print ("Você perdeu: %d" %diasPerdidos, "dias" )
