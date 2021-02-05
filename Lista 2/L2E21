#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1; Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

#Exercicio 21

valor = int(input("Informe o valor que deseja sacar: (10-600)"))

if valor > 600 or valor < 10:
  print("Valor invalido!")
  quit()
else:
  troco100 = int(valor / 100)
  valor = valor % 100

  troco50 = int(valor / 50)
  valor = valor % 50

  troco10 = int(valor / 10)
  valor = valor % 10

  troco5 = int(valor / 5)
  valor = valor % 5

  troco1 = valor

  print("Notas de 100: ", troco100)
  print("Notas de 50: ", troco50)
  print("Notas de 10: ", troco10)
  print("Notas de 5: ", troco5)
  print("Notas de 1: ", troco1)
