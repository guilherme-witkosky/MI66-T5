#Faça um Programa para leitura de três notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

#Exercicio 20

nota1 = float(input("Informe sua 1ª nota parcial: "))
nota2 = float(input("Informe sua 2ª nota parcial: "))
nota3 = float(input("Informe sua 3ª nota parcial: "))
media = ((nota1+nota2+nota3)/3)
print("====================================================")
print("Sua Nota Parcial = %.2f" % round(media,2))
if media >= 7 and media < 10:
    print("Situação: APROVADO!")
elif media < 7:
    print("Situação: REPROVADO!")
elif media == 10:
    print("Situação: APROVADO COM DISTINÇÃO!")
print("====================================================")
