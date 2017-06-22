'''

2) O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que o usuário informe o valor final do carro e o programa vai informar o custo de fábrica(quanto que foi para a fábrica), a percentagem do distribuidor em cima do valor total e o valor do imposto do carro.

custo de um carro novo = custo de fabrica + percentagem do distribuidor + impostos

percentagem do distribuidor = 28%
imposto= 45%
 100%
45 + 28 = 73 - 100 = 27
custo de fabrica = 27%

'''

a=int(input("Digite o Valor final do seu carro dos sonhos: "))

custo= a * 0.27
imposto= a * 0.45
distribuidor= a * 0.28

print("O Custo de fábrica do seu carro foi: ","%0.2f"%custo)
# 0 %0.2f , ele vai mostrar 0 casas antes da vírgula e 2 casas depois da virgula
print("A Percentagem do distribuidor do seu carro foi: ","%2.3f"% distribuidor)
# 0 %0.2f , ele vai mostrar 2 casas antes da vírgula(se tiver um numero só antes da virgula ele vai preencher com 0 a outra casa) e 2 casas depois da virgula
print("O Imposto aplicado em cima do seu carro foi: ","%d"% imposto)
# 0 %d , ele vai mostrar o o numero sem virgula, só a parte inteira)
