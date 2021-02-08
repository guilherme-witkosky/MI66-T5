#Faça um programa que leia 5 números e informe o maior número.
i = 0
vetNum = [0, 0, 0, 0, 0] 
maiorNumero = 0
while i < 5:
    vetNum[i] = input("Digite um numero:")
    i +=1

i = 0
while i < 5:
    if int(vetNum[i])>=int(maiorNumero):
        maiorNumero = vetNum[i]
    i +=1

print("O maior número digitado é:", maiorNumero)