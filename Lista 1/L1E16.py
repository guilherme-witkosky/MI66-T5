#Exercicio 16
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
#em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
#é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho = float(input("Informe quantos metros quadrados serão pintados:"))
qntnece = round(tamanho/3)
qtdlatas = round(qntnece/18)

if qtdlatas < 1:
  qtdlatas = 1 
  
valor = qtdlatas * 80
print("====================================================")
print("Tamanho Pintado = %.2f" % tamanho,"m²")
print("Quantidade de Latas: %.2f"% qtdlatas)
print("Preço Total = R$%.2f" % valor)
print("====================================================")
