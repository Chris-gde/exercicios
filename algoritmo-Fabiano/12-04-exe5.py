'''
5) o sistema deve perguntar a medida dos 3 lados de um triangulo, o sistema deve informar o tipo de triangulo: equilatero, isosceles ou escaleno.'
'''
print ('Informe os valores dos lados do triangulo')
lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))
  # Verifica o tipo de triangulo
if lado1 == lado2 and lado2 == lado3:
  print ('Triangulo Equilatero')
elif lado1 == lado2 or lado1 == lado2 or lado2 == lado3:
  print ('Triangulo Isosceles')
else:
  print ('Triangulo Escaleno')
