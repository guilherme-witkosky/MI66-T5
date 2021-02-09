#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
#Exercicio 12

altura = []
idade = []
maior = 0
total = 0
mais = 0

for x in range(4):
  idade.append(int(input("Informe a idade do aluno %d: " % (x+1))))
  altura.append(int(input("Informe a altura do aluno %d em cm: " % (x+1))))

for z in range (4):
     if idade[z] >= 13:
         total = (total + altura[z])
         mais += 1



for y in range(4):
    if idade[y] >= 13 and altura[y] < (total / mais):
        maior += 1

print(maior, "alunos com mais de 13 anos possuem altura inferior à média de altura")
