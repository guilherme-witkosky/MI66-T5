#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes,
# cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5%
# sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
# comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra:
#    tipo e quantidade de carne,
#    preço total,
#    tipo de pagamento,
#    valor do desconto
#    e valor a pagar.


print("                          PREÇOS                          ")
print("----------------------------------------------------------")
print("                          Até 5 Kg           Acima de 5 Kg")
print("1 - File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg")
print("2 - Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg")
print("3 - Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg")
print("----------------------------------------------------------")
tipoCarne = input("Informe a carne desejada: ")
pesoCarne = input("Informe o peso da carne: ")
cartao = input("Cartão tabajara 1-Sim 2-Não: ")

carne=""
precoCarne=0
desconto=0

valorTotal=0

if float(pesoCarne) > 5:
    if int(tipoCarne) == 1:
        precoCarne = 5.80
    elif int(tipoCarne) == 2:
        precoCarne = 6.80
    elif int(tipoCarne) == 3:
        precoCarne = 7.80
else:
    if int(tipoCarne) == 1:
        precoCarne = 4.90
    elif int(tipoCarne) == 2:
        precoCarne = 5.90
    elif int(tipoCarne) == 3:
        precoCarne = 6.90

if int(tipoCarne) == 1:
        carne="File Duplo"
    elif int(tipoCarne) == 2:
        carne="Alcatra"
    elif int(tipoCarne) == 3:
        carne="Picanha"

valorTotal=float(pesoCarne)*float(precoCarne)
 
if cartao == 1:
    desconto = valorTotal*0.05
else
    desconto = 0

valorTotal-=desconto

print("---Cupom Fiscal---")
print("Carne: ", carne)
print("Peso: Kg", pesoCarne)
print("Preço: R$", precoCarne)
print("Descontos: R$", )
print("Valor Total: ", valorTotal)
