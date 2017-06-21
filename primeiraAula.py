0) Faça um algoritmo que leia a data de nascimento(dia, mês e ano), e informe a idade correta
 
 diaNascimento=int(input("Informe seu dia de nascimento: "))
 mesNascimento=int(input("Informe seu mes de nascimento: "))
 anoNascimento=int(input("Informe ano de nascimento: "))
 
 anoAtual=2017
 mesAtual=6
 diaAtual=7
idade=anoAtual-anoNascimento

if mesAtual > mesNascimento:   
	idade=idade

elif mesNascimento == mesAtual and diaAtual >= diaNascimento:   
	idade=idade

else:   
	idade= idade-1
print("Sua idade é: ", idade)
