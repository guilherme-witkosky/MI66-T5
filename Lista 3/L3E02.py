#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
#Exercicio 2

while True:
    usuario = input("Informe seu usuario: ")
    senha = input("Informe sua senha: ")
    if usuario != senha:
      print("-------------------")
      print("Usuario: ", usuario)
      print("Senha: ", senha)
      break
    else: 
      print("Usuario e senha nao podem ser iguais!")
