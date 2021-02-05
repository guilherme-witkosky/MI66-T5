#Faça um Programa que leia três números e mostre-os em ordem decrescente.
num = float(input("Informe um numero:"))
num2 = float(input("Informe outro numero:"))
num3 = float(input("Informe outro numero:"))
if num >num2 and num>num3:
    print(num)
    if num2>num3:
     print(num2)
     print(num3)
    else:
     print(num3)
     print(num2)
elif num2>num3:
    print(num2)
    if num>num3:
     print(num)
     print(num3)
    else:
     print(num3)
     print(num)
else:
    print(num3)
    if num>num2:
     print(num)
     print(num2)
    else:
     print(num2)
     print(num)