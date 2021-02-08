# Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
# e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

flagContinua = 1
maiorTemp = 0
media =0
menorTemp = None
vetTemp = []
i = 0

while flagContinua == 1:
    vetTemp.append(float(input("Informe a temperatura: ")))
    if menorTemp == None:
        menorTemp = float(vetTemp[i])
        
    if float(vetTemp[i]) <= menorTemp:
        menorTemp = float(vetTemp[i])
        
    if vetTemp[i] >= maiorTemp:
        maiorTemp = float(vetTemp[i])
    
    media += vetTemp[i]
    
    flagContinua = int(input("Deseja cadastrar mais uma temperatura? 1-Sim 2-Não: "))
    i+= 1

media /= len(vetTemp)

print("A menor temperatura registrada: %.2f" % menorTemp)
print("A maior temperatura registrada: %.2f" % maiorTemp)

print("A media das temperaturas registradas: %.2f" % media)


