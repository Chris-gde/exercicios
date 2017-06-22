'''
3) - Determine se um ano é bissexto:
para ser bissexto, o ano deve ser:
	Divisível  4. Sendo assim, a divisão é exata com o resto igual a zero;
	Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
	Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
'''
def bissexto():

   ano =int(input ('ano:'))

   if ano%4 == 0:
       if ano%100 == 0:
           if ano%400 == 0:
               print('bissexto')
           else:
               print('nao bissexto')
       else:
           print('bissexto')
   else:
       print('nao bissexto')

if __name__=='__main__':
   bissexto()
