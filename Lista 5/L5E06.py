#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
#Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: 
# uma para fazer a conversão e uma para a saída. 
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões 
#terá um parâmetro formal para registrar se é A.M.
# ou P.M. 
# Inclua um loop que permita que o usuário repita esse cálculo 
# para novos valores de entrada todas as vezes que desejar.

periodo = ""
hora = 0
minuto = 0

def apresentaHorario(horaDia,minutoDia,periodoDia):
	if periodoDia.upper() == "A":
		periodoDia = " A.M."
	else: 
		periodoDia = " P.M."
	
	print("Horário")
	print(horaDia, ":",minutoDia, periodoDia)

def converteHora(horaDia,minutoDia,periodoDia):
	if horaDia == 13:
		horaDia = 1
	elif horaDia == 14:
		horaDia = 2
	elif horaDia == 15:
		horaDia = 3
	elif horaDia == 16:
		horaDia = 4
	elif horaDia == 17:
		horaDia = 5
	elif horaDia == 18:
		horaDia = 6
	elif horaDia == 19:
		horaDia = 7
	elif horaDia == 20:
		horaDia = 8
	elif horaDia == 21:
		horaDia = 9
	elif horaDia == 22:
		horaDia = 10
	elif hora == 23:
		horaDia = 11
	
	apresentaHorario(horaDia,minutoDia,periodoDia)	
	
hora = int(input("Informe a hora: "))
minuto = int(input("Informe os minutos: "))
periodo = input("Informe o periodo do dia: A - A.M. ou P - P.M.")

converteHora(hora,minuto,periodo)
