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
