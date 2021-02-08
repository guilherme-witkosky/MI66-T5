num = int(input("informe um numero inteiro:"))
fatorial = 1
x = num
while x>=1:
    print(x,".")
    fatorial = fatorial*x
    x -= 1
print("Valor total do Fatorial do %d = %d "%(num,fatorial))