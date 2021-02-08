#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
i = 0
vetNum = [0, 0] 

while i < 2:
    vetNum[i] = input("Informe o primeiro numero do intervalo:")
    i +=1

i = int(vetNum[0])
while i <= int(vetNum[1]):
    print(i)
    i+=1