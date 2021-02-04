#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

print("Digite sua altura:")
altura = input()

print("Digite H para homem ou M para mulher:")
genero = input()

if genero == "H":
    print("seu peso ideal seria: ", float((72.7*float(altura)) - 58))
elif genero == "M":
    print("seu peso ideal seria: ", float((62.1*float(altura)) - 44.7))
else:
    print("Caractere inválido")