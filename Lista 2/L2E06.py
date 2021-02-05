#Faça um Programa que leia três números e mostre o maior deles.
num = float(input("Informe um numero:"))
num2 = float(input("Informe outro numero:"))
num3 = float(input("Informe outro numero:"))
if num>num2 and num>num3 :
    print("O maior numero é o primeiro informado: ",num)
elif num2>num and num2>num3 :
    print("O maior numero é o segundo informado: ",num2)
else:
    print("O maior numero é o terceiro informado: ",num3)

