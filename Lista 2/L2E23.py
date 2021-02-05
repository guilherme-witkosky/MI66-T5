#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

#Exercicio 23

num = float(input("Informe um numero para saber se é inteiro ou decimal: "))

if num == round(num):
  print(num, "é inteiro")
else:
  print(num, "é decimal")
