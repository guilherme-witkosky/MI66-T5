#Exercico 27

print("           |        Até 5 Kg        |   Acima de 5 Kg  ")
print("           |                        |                  ")
print("Morango    |     R$ 2,50 por Kg     |    R$ 2,20 por Kg")
print("           |                        |                  ")
print("Maçã       |     R$ 1,80 por Kg     |    R$ 1,50 por Kg")
print("-------------------------------------------------------")

morango = float(input("Informe quantos Kg de morango deseja: "))

if morango < 0:
  print("Valor invalido")
  quit()

elif morango <= 5:
  valor1 = (morango * 2.5)

else:
  valor1 = (morango * 2.2)

#----------------------

maca = float(input("Informe quantos Kg de maça deseja: "))

if maca < 0:
  print("Valor invalido")
  quit()

elif maca <= 5:
  valor2 = (maca * 1.8)

else:
  valor2 = (maca * 1.5)

if (morango + maca) > 8 or (valor1 + valor2) > 25:
  valorTot = (valor1 + valor2) * 10 / 100
  valorTot = (valor1 + valor2) - valorTot
  print("Valor total - R$", valorTot)
  print("Morango: ", morango, "Kg")
  print("Maçã: ", maca, "Kg")

else:
  print("Valor total - R$", (valor1 + valor2))
  print("Morango: ", morango, "Kg")
  print("Maçã: ", maca, "Kg")
