#Exercício 15 
#Faça um Programa que pergunte quanto você ganha por horas
#e o número de horas trabalhadas no mês. Calcule e mostre
#o total do seu salário no referido mês, sabendo-se que são
#descontados 11% para o Imposto de Renda, 8% para o INSS e 
#5% para o sindicato, faça um programa que nos dê:
#*Salário Bruto.
#*Quanto Pagou ao INSS.
#*Quanto Pagou ao Sindicato.
#*Salário Líquido.

print("Informe quanto você ganha por hora: ")
valorhora = float(input())
print("Informe quantas horas você trabalhou esse mês: ")
horas = float(input())
salariobruto = (valorhora * horas)
ir = (salariobruto * 0.11)
inss = (salariobruto * 0.08)
sindicato = (salariobruto * 0.05)
descontos = (ir+inss+sindicato)
salarioliquido = (salariobruto - descontos)
print("====================================================")
print("Salário Bruto = R$ %.2f" % round(salariobruto,2))
print("Valor Pago ao Imposto de Renda = R$ %.2f" % round(ir,2))
print("Valor Pago ao INSS = R$ %.2f" % round(inss,2))
print("Valor Pago ao Sindicato = R$ %.2f" % round(sindicato,2))
print("----------------------------------------------------")
print("Salário Líquido = R$ %.2f" % round(salarioliquido,2))
print("====================================================")