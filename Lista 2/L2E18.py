#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine 
#se a mesma é uma data válida.

data = input("Informe uma data no formato dd/mm/aaaa: ")

dataSeparada = data.split("/")

dia = dataSeparada[0]
mes = dataSeparada[1]
ano = dataSeparada[2]

dataValida = True

if int(mes) == 04 and int(mes) == 06 and int(mes) == 09 and int(mes) == 11 
    if int(dia) <=0 or int(dia) >30 >:
        dataValida = False
else:
    if int(dia) <=0 or int(dia) >31 >:
        dataValida = False


if int(ano) % 100 != 0 and int(ano) % 4 == 0 or int(ano) % 400 == 0:
    if int(dia) <=0 or int(dia) > 29:
        dataValida = False
elif int(mes) == 02:
    if int(dia) <=0 or int(dia) > 28:
        dataValida = False
        
if int(mes) < 01 and int(mes) > 12
    dataValida = False

if int(mes) < 1 and int(mes) > 2021
    dataValida = False

print("data valida: ", dataValida)