#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
#O usuário deverá informar a quantidade de CDs e o valor para em cada um.

i = 0

qtdCd = int(input("Informe a quantidade de cd's em sua coleção:"))
valorTotal =0.00
media = 0.00

while i < qtdCd:
    print("Cd ", (i+1))
    vetNum.append(float(input("Informe o valor cd:")))
    valorTotal += float(vetNum[i])
    media += float(vetNum[i])
    i +=1

media /= qtdCd

print("Valor total da coleção: R$", valorTotal)
print("Valor medio gasto: R$", media)
