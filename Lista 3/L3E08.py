i = 0
vetNum = [0, 0, 0, 0, 0] 
soma = 0
media = 0
while i < 5:
    vetNum[i] = input("Digite um numero:")
    i +=1

i = 0
while i < 5:
    soma += float(vetNum[i])
    media += float(vetNum[i])
    i +=1
    
media /= 5
    
print("A soma dos números é:",soma)
print("A média dos números é:",media)
