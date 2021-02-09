#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
    
i = 0
letras = []

while i < 10:
    letras.append(input("Digite um caractere: "))
    i +=1
    
i = 0
while i < 10:
    if letras[i].upper() == "A" or letras[i].upper() == "E" or letras[i].upper() == "I" or letras[i].upper() == "O" or letras[i].upper() == "U":
        print(letras[i])
    i+=1
    