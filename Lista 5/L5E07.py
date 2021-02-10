#Faça um programa que use a função valorPagamento para determinar o valor 
#a ser pago por uma prestação de uma conta. 
#O programa deverá solicitar ao usuário o valor da prestação 
#e o número de dias em atraso e passar estes valores para a função valorPagamento,
# que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela.
# Após a execução o programa deverá voltar a pedir outro valor de prestação 
# e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia,
# que conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,
# cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa,
# mais 0,1% de juros por dia de atraso.

valorPrestacao = 0.00
diasAtraso = 0
valorTotalPrestacao = 0.00
qtdPrestacao = 0
flagContinua = True

def valorPagamento(prestacao,dias):
	if dias == 0:
		return prestacao
	else:
		juros = prestacao*((3+(dias*0.01))/100)
		print("Juros: ",juros)
		prestacao += juros
		return prestacao
		
while flagContinua:
	qtdPrestacao+=1
	valorPrestacao = float(input("Informe o valor da prestacao: "))
	
	if valorPrestacao == 0:
		flagContinua = False
		break
	
	diasAtraso = int(input("Informe a quantidade de dias em atraso: "))
		
	print("Valor a ser pago: ", valorPagamento(valorPrestacao,diasAtraso))
	valorTotalPrestacao+= valorPagamento(valorPrestacao,diasAtraso)

print("Relatório do dia")
print("Prestações pagas: ", qtdPrestacao)
print("Valor total das prestações: ", valorTotalPrestacao)
	