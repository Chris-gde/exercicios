'''
2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
usuario=input("Digite seu usuário: ")
senha= input("Digite sua senha: ")
if usuario==senha :
    print("Usuario não pode ser igual a senha!!!!")
    usuario=input("Digite seu usuário: ")
    senha= input("Digite sua senha: ")
print("Acesso garantido")
