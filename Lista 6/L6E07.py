mensagem = input("Informe uma mensagem:")
conSpaces = 0
conVogais = 0
for x in range(len(mensagem)):
    if mensagem[x] == " ":
     conSpaces +=1
    if mensagem[x].lower()  == "a" or mensagem[x].lower()  == "e" or \
    mensagem[x].lower()  == "i" or mensagem[x].lower()  == "o" or mensagem[x].lower()  == "u":
     conVogais +=1
print("A mensagem contem ",conSpaces," espaço(s) em branco.")
if conVogais == 1:
    print("A mensagem contem ",conVogais," vogal.")
else:
    print("A mensagem contem",conVogais," vogais")