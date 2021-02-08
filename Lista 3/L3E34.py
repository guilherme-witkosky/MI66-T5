#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
#Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Informe um numero: "))
if num < 2: 
    print('O numero não é primo')
    
elif num == 2: 
    print('O numero é primo')
    
elif num % 2 == 0: 
    print('O numero não é primo')
    quit()
else: 
    for i in range(3, num // 2, 2):
        if num % i == 0:
            print('O numero não é primo')
            break
    else:
        print('O numero é primo')