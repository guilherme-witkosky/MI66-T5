#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos 
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

fruta1 = input("Informe o peso dos morangos: ")
fruta2 = input("Informe o peso dos morangos: ")

precofruta1 = 0
precofruta2 = 0

pesoTotal = float(fruta1)+float(fruta2)
desconto=0

valorTotal=0

if float(pesoTotal) > 8:
    desconto=0.1

if float(fruta1) < 5:
    precofruta1 = 2.50
else:
    precofruta1 = 2.20
    
if float(fruta2) < 5:
    precofruta2 = 1.80
else:
    precofruta2 = 1.50
    
valorTotal=(float(fruta1)*float(precofruta1)+float(fruta2)*float(precofruta2))
valorTotal=valorTotal-(valorTotal*desconto)

print("---Cupom Fiscal---")
print("Morango: Kg", fruta1)
print("Maçã: Kg", fruta2)
print("Descontos: ", float(desconto)*100)
print("Valor Total: ", valorTotal)