'''
4) Altere o exercício e armazene num vetor as idades informadas.
'''
a=int(input(" Informe quantas idades serão informadas "))

cont = 0
idades=[]
while cont<a:
    i=int(input(" Digite a sua idade: "))
    idades.append(i)
    cont = cont + 1
print(idades)
