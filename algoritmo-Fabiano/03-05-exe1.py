'''
(1) - Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa
'''
valor_da_conta = float(input('Entre com o valor da conta: '))
troco = [50,20, 10, 5, 2, 1]
cont = 0
while valor_da_conta > 0:
   n = valor_da_conta/troco[cont]
   valor_da_conta = valor_da_conta%troco[cont]
   if n != 0:
      print('%d notas de R$ %.2f' %(n, troco[cont]))
   cont += 1

#Logica: imprime o troco até chegar o valor da conta que foi digitado pelo "caixa"
