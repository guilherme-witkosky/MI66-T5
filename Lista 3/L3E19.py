#Exercício 19
quant = int(input("INFORME A QUANTIDADE DO CONJUNTO DOS NÚMEROS: "))
menor = 1000
maior = 0
soma = 0
cont = 1

while cont <= quant:
  print("----------------------------------------------------------")
  num = int(input("INSIRA UM NÚMERO ENTRE 0 E 1000: "))
  if num < 0 or num > 1000:
    print("VALOR INVÁLIDO, INSIRA UM NUMERAL ENTRE 0 E 1000")
  else:
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