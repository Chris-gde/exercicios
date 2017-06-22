'''
2) Faça um algoritmo que o usuário informe quantas idades serão informadas e exiba a maior.
'''
i=int(input("Informe quantas idades serão informadas "))
m=0
cont=0
while cont<i:
    a=int(input("Digite a sua idade: "))
    if a>m:
        m=a
    cont=cont+1
print(m)
