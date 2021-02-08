#Exercício 14
cont = 1
soma = 0
par = 0
impar = 0
while cont <= 10:
  num = int(input(print("INFORME O ",cont,"° NÚMERO: ")))
  soma += num
  if (num % 2) == 0:
    par += 1
  else:
    impar += 1
  cont += 31
print("=========================================")
print("A SOMA DOS 10 NÚMEROS É ",soma)
print("-----------------------------------------")
print("NÚMEROS PARES: ",par)
print("NÚMEROS IMPARES: ", impar)
print("=========================================")