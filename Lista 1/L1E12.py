#Exercicio
#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
#(72.7*altura) - 58
altura = float(input("Informe a sua altura:"))
peso_ideal = (72.7*altura)-58
print("O peso ideal para sua altura é: %.2f" % peso_ideal)
