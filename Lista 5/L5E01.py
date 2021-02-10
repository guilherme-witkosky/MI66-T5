#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
#Exercicio 1

valor = (int(input("Informe o valor de n: ")))

def exec1(n):
    for x in range(n):
        x += 1
        print(str(x) * x)

exec1(valor)
