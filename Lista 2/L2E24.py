#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual int(oper)ação ele deseja 
#realizar. O resultado da int(oper)ação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.


num1 = input("Informe o numero 1: ")
num2 = input("Informe o numero 2: ")

resultado = 0

parImpar = ""
positivoNegativo = ""
inteiroDecimal = ""

oper = input("Informe a int(oper)ação 1-Somar 2-Subtrair 3-Multiplicar 4-Dividir: ")

if int(oper) == 1:
    resultado = float(num1)+float(num2)
elif int(oper) == 2:
    resultado = float(num1)-float(num2)
elif int(oper) == 3:
    resultado = float(num1)*float(num2)
elif int(oper) == 4:
   resultado = float(num1)/float(num2)
else:
    print("caractere inválido")
    quit()

if resultado % 2==0:
    parImpar = "Par"
else:
    parImpar = "Impar"
    
if resultado > 0:
    positivoNegativo = "Positivo"
else:
    positivoNegativo = "Negativo"
    
if resultado == round(resultado):
    inteiroDecimal = "Inteiro"
else:
    inteiroDecimal = "Decimal"
    
print("Resultado: ", resultado)
print("Par ou ímpar: ", parImpar)
print("Positivo ou Negativo: ", positivoNegativo)
print("Inteiro ou Decimal: ", inteiroDecimal)