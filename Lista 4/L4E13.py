temp= []
mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
media = 0
for x in range(12):
    print("informe a temperatura de ",mes[x])
    temp.append((float(input())))
media = sum(temp)/len(temp)
print("A média anual de temperatura foi %.2f:" % media)
for y in range(12):
    if temp[y]>=media:
        print("O mês de ",mes[y],"teve a temperatura acima da média com:%.2f °C"%temp[y])