i = 0
carro = []
consumo = []
maisEconomico = None
auxEconomico = 0

while i < 5:
    print("Veiculo", (i+1))
    carro.append(input("Nome: "))
    consumo.append(float(input("Km por litro: ")))
    if maisEconomico == None:
        maisEconomico = i
        auxEconomico = consumo[i]
    if auxEconomico <= consumo[i]:
        maisEconomico = i
        auxEconomico = consumo[i]
    i +=1


print("Relatório Final")
i = 0
while i < 5:
    print((i+1), " - ", carro[i], " - ", consumo[i], " - ", (1000/consumo[i]),(1000/consumo[i])*2.25)
    i+=1
print("O menor consumo é do ",carro[maisEconomico])    