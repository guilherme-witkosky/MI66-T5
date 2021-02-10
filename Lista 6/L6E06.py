#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
#Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
#Exercicio 11 

data = input("Informe sua data de nascimento: [dd/mm/aaaa]: ")

d = int(data[0] + data[1])
m = int(data[3] + data[4])
a = int(data[6] + data[7] + data[8] + data[9])


def exe6(d, m , a):

    if d > 31 or d <= 0:
        print("Dia invalido")
        exit()

    if m > 12 or m <= 0:
        print("Mes invalido")
        exit()

    if m == 1:
        print(d, " de Janeiro de ", a) 

    elif m == 2:
        print(d, " de Fevereiro de ", a)

    elif m == 3:
        print(d, " de Março de ", a)

    elif m == 4:
        print(d, " de Abril de ", a)

    elif m == 5:
        print(d, " de Maio de ", a)

    elif m == 6:
        print(d, " de Junho de ", a)

    elif m == 7:
        print(d, " de Julho de ", a)

    elif m == 8:
        print(d, " de Agosto de ", a)

    elif m == 9:
        print(d, " de Setembro de ", a)

    elif m == 10:
        print(d, " de Outubro de ", a)

    elif m == 11:
        print(d, " de Novembro de ", a)

    elif m == 12:
        print(d, " de Dezembro de ", a)

exe6(d, m, a)
