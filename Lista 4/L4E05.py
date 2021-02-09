lista= []
listaImp = []
listaPar = []
for x in range(20):
    lista.append(int(input("Informe um numero inteiro:")))
    if lista[x] % 2 == 0:
        listaPar.append(lista[x]) 
    else:
        listaImp.append(lista[x])
print("--------------  Lista com os 20 valores --------------------------------")
print(lista)
print("--------------- Lista com os valores Impares ---------------------------")
print(listaImp)
print("--------------  Lista com os valores Pares -----------------------------")
print(listaPar)