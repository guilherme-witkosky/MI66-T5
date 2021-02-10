
def numero():
    m = int(input("Informe um numero inteiro:"))
    for x in range(1,m+1):
        for z in range(1,x+1):
            print(z," ",end="")
        print("") 
numero() 
