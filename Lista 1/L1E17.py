#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

valorLata = 25
valorGalao = 80

print("Digite o valor da área a ser pintada:")
area = input()

quantidadeTinta = float((float(area)/6)*1.1)

quantidadeLata = math.ceil(float(quantidadeTinta)/3.6)
quantidadeGalao = math.ceil(float(quantidadeTinta)/18)

print(f"Quantidade de tinta a ser usada: {quantidadeTinta:.2f}L")

print("Resultado: ")
print("Quantidade de Latas 3,6L: ",quantidadeLata)
print("Quantidade de Galões 18L: ",quantidadeGalao)

print("Valor em Latas 3,6L: R$",(float(quantidadeLata) * float(valorLata)))
print("Valor em Galões 18L: R$",(float(quantidadeGalao) * float(valorGalao)))

quantidadeGalaoMisto = float(float(quantidadeTinta//18))
quantidadeLataMisto = math.ceil((float(quantidadeTinta)-float(quantidadeGalaoMisto)*18)/3.6)
valorGalaoMisto = float(float(quantidadeGalaoMisto)*80)
valorLataoMisto = float(float(quantidadeLataMisto)*25)

print("Quantidade de Latas 3,6L Misto: ",quantidadeLataMisto)
print("Quantidade de Galões 18L Misto: ",quantidadeGalaoMisto)
print("Valor Misto: R$", float(float(valorGalaoMisto) + float(valorLataoMisto)))
