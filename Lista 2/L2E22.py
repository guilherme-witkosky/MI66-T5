#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

#Exercicio 22

num = int(input("Digite um numero para ver se ele é par ou nao: "))

if (num % 2) == 0:
  print(num, "eh par")
else:
  print(num, "eh impar")
