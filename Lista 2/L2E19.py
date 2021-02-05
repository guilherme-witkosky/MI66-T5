#Faça um Programa que leia um número inteiro menor que 1000 e imprima
#a quantidade de centenas, dezenas e unidades do mesmo. Observando os
#termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades Testar com: 
#326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

#Exercício 19

num1 = int(input("Digite um numero ate 1000: "))
if num1>=1000:
  print("Numero invalido")

else:
  string = str(num1)
  qtdNum = len(string)

  if qtdNum == 3:
    centena = string[0:1]
    dezena = string[1:2]
    unidade = string[2:3]

    print("Centena: ", centena,"| Dezena: ", dezena,"| Unidade: ", unidade)

  if qtdNum == 1:
    dezena = string[0:1]
    unidade = string[1:2]
    
    print("Dezena: ", dezena,"| Unidade: ", unidade)

  if qtdNum == 1:
    unidade = string[0:1]

    print("Unidade: ", unidade)
