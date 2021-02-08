#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
#Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Informe um numero: "))

i = 0
while i <= num:
    if i < 2: 
        print("O numero i não é primo")
        
    if i == 2: 
        print('O numero é primo')
        
    if i % 2 == 0: 
        print('O numero não é primo')
    else: 
        for x in range(3, num // 2, 2):
            if num % x == 0:
                print('O numero não é primo')
                break
        else:
            print('O numero é primo')