#Exercício 18
quant = int(input("INFORME A QUANTIDADE DO CONJUNTO DOS NÚMEROS: "))
menor = 999999999
maior = 0
soma = 0
cont = 1
print("----------------------------------------------------------")
while cont <= quant:
  num = int(input("INSIRA UM NÚMERO: "))
  soma += num
  if num <= menor:
    menor = num
  if num >= maior:
    maior = num
  cont += 1
print("==========================================================")
print("A SOMA DOS NÚMEROS INFORMADOS É ",soma)
print("----------------------------------------------------------")
print("O MENOR NÚMERO INFORMADO FOI ",menor)
print("O MAIOR NÚMERO INFORMADO FOI ",maior)
print("==========================================================")