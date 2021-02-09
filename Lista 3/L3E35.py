
num = int(input("Informe um numero: "))

i = 0
while i <= num:
    if i < 2: 
        print("O numero ", i," não é primo")
        
    elif i == 2: 
        print("O numero ", i," é primo")
        
    elif i % 2 == 0: 
        print("O numero ", i," não é primo")
    else: 
        for x in range(3, num // 2, 2):
            if num % x == 0:
                print("O numero ", i," não é primo")
                break
        else:
            print("O numero ", i," é primo")
    i+=1
