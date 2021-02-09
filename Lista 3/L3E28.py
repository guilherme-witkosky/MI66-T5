i = 0

qtdCd = int(input("Informe a quantidade de cd's em sua coleção:"))
valorTotal =0.00
media = 0.00
vetNum = []

while i < qtdCd:
    print("Cd ", (i+1))
    vetNum.append(float(input("Informe o valor cd:")))
    valorTotal += float(vetNum[i])
    media += float(vetNum[i])
    i +=1

media /= qtdCd

print("Valor total da coleção: R$", valorTotal)
print("Valor medio gasto: R$", media)
