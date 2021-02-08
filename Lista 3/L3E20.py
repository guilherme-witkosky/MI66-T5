sair = True
while sair:
    num = int(input("informe um numero inteiro:"))
    if num <16:
        fatorial = 1
        x = num
        while x>=1:
            print(x,".")
            fatorial = fatorial*x
            x -= 1
        print("Valor total do Fatorial do %d = %d "%(num,fatorial))
    else:
        print("Número inválido!!")
    sair = input("deseja sair? s ou n:")
    
    if sair.upper() == "S":
        sair = False
        print("Programa Encerrado")