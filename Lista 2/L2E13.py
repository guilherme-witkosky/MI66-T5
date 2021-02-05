#Faça um Programa que leia um número e exiba o dia correspondente
#da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor
#deve aparecer valor inválido.

#Exercício 13
num = input("Infome um numero e o sistema mostrará um dia da semana: ")
if num is "1":
  print("Domingo")
elif num is "2":
  print("Segunda-Feira")
elif num is "3":
  print("Terça-Feira")
elif num is "4":
  print("Quarta-Feira")
elif num is "5":
  print("Quinta-Feira")
elif num is "6":
  print("Sexta-Feira")
elif num is "7":
  print("Sábado")
else:
  print("Valor invalido!!")
