#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0
#Exercicio 6

nota = 0
listaNotas = []
acima = 0

for x in range(2):
    print("Aluno %d: " % (x+1))
    total = 0

    for y in range(4):
        nota = input("Informe a nota do aluno: ")
        total += float(nota)

    total /=4
    listaNotas.append(total)

for z in range(2):
    if listaNotas[z] >= 7:
        acima += 1
print("----------------------------")
print(acima, "alunos foram aprovados!")
