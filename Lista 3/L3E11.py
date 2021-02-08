#Exercício 11
num1 = input("Informe o primeiro número: ")
num2 = input("Informe o último número: ")
soma = 0
if int(num1) <= int(num2):
  primeiro = int(num1)
  ultimo = int(num2)
else:
  primeiro = int(num2)
  ultimo = int(num1)
while primeiro <= ultimo:
    soma = soma + primeiro
    primeiro += 1
print("================================================================")
print("Resultado = ", soma)
print("================================================================")