#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
    
i = 0
numeros = []
soma = 0
multi = 1

while i < 5:
    numeros.append(float(input("Digite um número: ")))
    soma+=numeros[i]
    multi*=numeros[i]
    i +=1
    
i = 0
while i < 5:
    print(numeros[i], " ", end="")
    i+=1
print("")
print("Soma: ", soma)
print("Multiplicação: ", multi)
    