posicao = ["Primeiro","Segundo","Terceiro","Quarto","Quinto"]
salto= [0] * 5
media = 0
nome = " "
while nome != '':
    nome = input("Atleta: ")
    if nome =='':
        break
    for x in range(5):
        print("%s Salto:"%(posicao[x]))
        salto[x]= ((float(input())))
    media = sum(salto)/len(salto)
    print("Resultado final:")
    print("Atleta:",nome)
    print("Saltos:",salto[0]," - ",salto[1]," - ",salto[2]," - ",salto[3]," - ",salto[4])
    print("Média dos saltos %.2f m:"%media)
    
    print("-----------------------------------------------------")