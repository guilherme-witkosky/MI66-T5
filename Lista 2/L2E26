#Um posto está vendendo combustíveis com a seguinte tabela de descontos: Álcool: até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R 2,50opreçodolitrodoálcooléR  1,90.

#Exercicio 26

escolha = input("Informe o tipo de gasolina: (A- álcool | G- gasolina)")

if escolha.lower() == "a":
  litros = float(input("Informe os litros que deseja: "))
  if litros < 0:
    quit()
  elif litros <= 20:
    desconto = (litros * 3) / 100
    litros = litros - desconto 
    valor = (litros * 1.90)
    print("R$: ", valor)
  else:
    desconto = (litros * 5) / 100
    litros = litros - desconto
    valor = (litros * 1.90)
    print("R$: ", valor)
elif escolha.lower() == "g":
  litros = float(input("Informe os litros que deseja: "))
  if litros < 0:
    quit()
  elif litros <= 20:
    desconto = (litros * 4) / 100
    litros = litros - desconto 
    valor = (litros * 2.5)
    print("R$: ", valor)
  else:
    desconto = (litros * 6) / 100
    litros = litros - desconto
    valor = (litros * 2.5)
    print("R$: ", valor)

else:
  print("Opção invalida")
