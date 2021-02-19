#Faça um programa que calcule o mostre a média aritmética de N notas.
#Exercicio 24
notas = []
soma = 0.0
nota=0.0
print("Informe um numero maior do que 10 ou menor que 0 para sair.")
while True:
    nota=(float(input("Informe a nota:")))
    if nota < 0 or nota>10:
          break;
    else:
        notas.append(nota)
        soma = 0
    for x in range(len(notas)):
        soma +=notas[x] 
    
if len(notas)>0:
    print("A média aritmetica das notas são:",(soma/(len(notas))))
