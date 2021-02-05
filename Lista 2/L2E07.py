#Faça um Programa que leia três números e mostre o maior e o menor deles.
#Exercícios 7
num = float(input("Informe um numero:"))
num2 = float(input("Informe outro numero:"))
num3 = float(input("Informe outro numero:"))
if num>num2 and num>num3 :
    print("O maior numero é o : ",num)
elif num2>num and num2>num3 :
    print("O maior numero é o : ",num2)
else:
    print("O maior numero é o : ",num3)
if num<num2 and num<num3 :
    print("O menor numero é o : ",num)
elif num2<num and num2<num3 :
    print("O menor numero é o : ",num2)
else:
    print("O menor numero é o : ",num3)