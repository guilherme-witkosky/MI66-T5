#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
    
i = 0
idade = []
altura = []

while i < 5:
    idade.append(int(input("Informe a idade: ")))
    altura.append(float(input("Informe a altura: ")))
    i +=1
    
i = 4
while i >= 0:
    print("Idade: ",idade[i], " ", end="")
    print("Altura: ",altura[i], " ",)
    i-=1
    