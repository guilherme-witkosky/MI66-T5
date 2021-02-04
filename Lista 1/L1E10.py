#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print("Digite o valor a ser transformado para Fahrenheit:")
grausCelsius = input()

grausTransformados = (float(grausCelsius) * 9/5 + 32)
print("Graus Celsius:", grausCelsius)
print("Graus Fahrenheit:", grausTransformados)