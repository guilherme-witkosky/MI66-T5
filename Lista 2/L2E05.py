#Exercício 5
nota1 = float(input("Informe sua 1ª nota parcial: "))
nota2 = float(input("Informe sua 2ª nota parcial: "))
media = ((nota1+nota2)/2)
print("====================================================")
print("Sua Nota Parcial = %.2f" % round(media,2))
if media >= 7 and media < 10:
    print("Situação: APROVADO!")
elif media < 7:
    print("Situação: REPROVADO!")
elif media == 10:
    print("Situação: APROVADO COM DISTINÇÃO!")
print("====================================================")
