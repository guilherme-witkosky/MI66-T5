#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% 

#Após o aumento ser realizado,informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = input("Informe seu salário:")

salarioReajuste = 0
percentual = 0
valorReajuste = 0;

if float(salario) < 280:
    percentual = "20%"
    salarioReajuste = float(salario)*1.2
    valorReajuste = float(salarioReajuste)-float(salario)
elif float(salario) >= 280 and float(salario) < 700:
    percentual = "15%"
    salarioReajuste = float(salario)*1.15
    valorReajuste = float(salarioReajuste)-float(salario)
elif float(salario) >= 700 and float(salario) < 1500:
    percentual = "10%"
    salarioReajuste = float(salario)*1.1
    valorReajuste = float(salarioReajuste)-float(salario)
else:
    percentual = "5%"
    salarioReajuste = float(salario)*1.05
    valorReajuste = float(salarioReajuste)-float(salario)
    
print("Resultado: ")
print("Salário antes do reajuste: R$", salario)
print("Percentual de aumento aplicado: ", percentual)
print("Valor do aumento: R$", valorReajuste)
print("Salario com aumento aplicado: R$", salarioReajuste)