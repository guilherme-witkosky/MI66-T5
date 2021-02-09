#14 Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
#Exercicio 14

perguntas = []
per = []
clas = 0

per.append(input("Telefonou para a vítima? [s/n]"))
per.append(input("Esteve no local do crime? [s/n]"))
per.append(input("Mora perto da vítima? [s/n]"))
per.append(input("Devia para a vítima? [s/n]"))
per.append(input("Já trabalhou com a vítima? [s/n]"))

for x in range(5):
  if per[x].lower() == "s":
    clas += 1

if clas == 2:
    print("Suspeito")
elif clas == 3 or clas == 4:
    print("Cumplice")
elif clas == 5:
    print("Assasino")
else: 
    print("Inocente")


