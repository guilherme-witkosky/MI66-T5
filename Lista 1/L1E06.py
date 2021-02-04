#Exercício 6 
#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
print("Informe o raio do círculo:")
raio = float(input())
pi = math.pi
area = (pi * (raio * raio))
print("A área do círculo é ",area)