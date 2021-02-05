#Faça um programa que lê as duas notas parciais obtidas por um aluno 
#numa disciplina ao longo de um semestre, e calcule a sua média. 
#A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0        A
#Entre 7.5 e 9.0         B
#Entre 6.0 e 7.5         C
#Entre 4.0 e 6.0         D
#Entre 4.0 e zero        E
#Exercício 14

nota1 = float(input("Informe sua 1ª nota parcial: "))
nota2 = float(input("Informe sua 2ª nota parcial: "))
media = ((nota1 + nota2)/2)
print("================================================")
print("Média Parcial = %.2f" % round(media,2))
if media >= 9:
  print("Conceito Parcial = A")
elif media >= 7.5 and media < 9:
  print("Conceito Parcial = B")
elif media >= 6 and media < 7.5:
  print("Conceito Parcial = C")
elif media >= 4 and media < 6:
  print("Conceito Parcial = D")
elif media < 4:
  print("Conceito Parcial = E")
print("================================================")
