#Exercício 22
print("=======================================================================")
num = int(input("DIGITE UM NÚMERO INTEIRO: "))
cont = 0
div = []
print("-----------------------------------------------------------------------")
for i in range(num):
    if num%(i+1) == 0:
        cont += 1
        div.append(i+1)
    else:
        cont
if cont == 2:
    print ("O NÚMERO É PRIMO DIVISÍVEL POR ",div)
else:
    print ("O NÚMERO NÃO É PRIMO, POIS É DIVISÍVEL POR ",div)
print("=======================================================================")