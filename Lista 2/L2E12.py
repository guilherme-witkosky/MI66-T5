#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
#e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

valorHora = input("Informe o valor da hora trabalhada:")
horas = input("Informe as horas trabalhadas:")

IR = 0
INSS = 0
FGTS = 0;
totalDescontos = 0
percentualIR = "0%"
salarioBruto = float(valorHora)*float(horas)
salarioLiquido = float(salarioBruto)*float(horas)

if float(salarioBruto) <= 900:
    IR = 0
    INSS = float(salarioBruto)*0.1
    FGTS = float(salarioBruto)*0.11
    totalDescontos = float(IR)+float(INSS)
    salarioLiquido = float(salarioBruto)-float(totalDescontos)
elif float(salarioBruto) <= 1500:
    IR = float(salarioBruto)*0.05
    INSS = float(salarioBruto)*0.1
    FGTS = float(salarioBruto)*0.11
    totalDescontos = float(IR)+float(INSS)
    salarioLiquido = float(salarioBruto)-float(totalDescontos)
elif float(salarioBruto) <= 2500:
    IR = float(salarioBruto)*0.1
    INSS = float(salarioBruto)*0.1
    FGTS = float(salarioBruto)*0.11
    totalDescontos = float(IR)+float(INSS)
    salarioLiquido = float(salarioBruto)-float(totalDescontos)
elif float(salarioBruto) > 2500:
    IR = float(salarioBruto)*0.2
    INSS = float(salarioBruto)*0.1
    FGTS = float(salarioBruto)*0.11
    totalDescontos = float(IR)+float(INSS)
    salarioLiquido = float(salarioBruto)-float(totalDescontos)
    
print("Folha de pagamento: ")
print("Salario Bruto: R$", salarioBruto)
print("(-) IR : R$", IR)
print("(-) INSS ( 10%): R$", INSS)
print("FGTS (11%): R$", FGTS)
print("Total de Descontos: R$", totalDescontos)
print("Salário Liquido: R$", salarioLiquido)