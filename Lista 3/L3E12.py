num = int(input("informe um numero entre 1 a 10:"))
if num <1 or num >10:
    print("Numero informado inválido fechando o programa!!")
else:
    print("Tabuada de ",num,":")
    for x in range(11):
        print("%d X %d = %d" %(num,x,(num*x)))