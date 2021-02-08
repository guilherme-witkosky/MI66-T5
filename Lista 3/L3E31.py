#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
#Faça um programa que implemente uma caixa registradora rudimentar. 
#O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
#Um valor zero deve ser informado pelo operador para indicar o final da compra. 
#O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
#para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
#para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#Lojas Tabajara 
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00
#...

flagContinua = True

valorProd = []
valorTotal = 0.00

i = 0
while flagContinua:
    valorProd.append(float(input("Informe o valor do produto: ")))
    if valorProd[i] == 0:
        flagContinua = False
    i +=1

i = 0

while i < len(valorProd):
    print("Produto ", (i+1),": R$", valorProd[i])
    valorTotal += valorProd[i]
    i+=1

print("Total: R$%.2f" % valorTotal)
pag = input("Dinheiro: R$")
print(f"Troco: R$%.2f" %(float(pag)-float(valorTotal)))
