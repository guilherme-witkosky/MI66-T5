#Faça um Programa que verifique se uma letra digitada
# é "F" ou "M". Conforme a letra escrever: 
#F - Feminino
#M - Masculino
#Sexo Inválido.

#Exercício 3
sexo = input("Informe uma letra :")
if sexo.upper() == "M":
    print("O sexo informado foi MASCULINO")
elif sexo.upper() == 'F':
    print("O sexo informado foi FEMININO")
else:
    print("O sexo Inválido")