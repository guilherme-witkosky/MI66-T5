#Exercício 21
print("==================================================")
num = int(input("DIGITE UM NÚMERO INTEIRO: "))
cont = 0
i = 0
print("--------------------------------------------------")
while i <= num or cont < 2:
  i = i + 1
  x = num % i
  if x == 0:
    cont = cont + 1
if cont <= 2:
  print("PRIMO")
else:
  print("NÃO PRIMO")
print("==================================================")