import random

palavras = ["ARROZ", "OVO", "JAVA", "VERMELHO", "AZUL"]

linhas = ""
palavraForca = ""
validaLetra = False
completou = False
erros = 0
acertos = 0

def replacer(s, newstring, index, nofail=False):
    
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    
    if index < 0: 
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

x = random.randint(1,5)

i = 0
while i < len(palavras[x]):
	linhas+="-"
	i+=1

while completou == False:
	letra = input("Digite uma letra: ")
	
	letra = letra.upper()
	
	i = 0
	while i < len(list(palavras[x])):
		if list(palavras[x])[i].upper() == letra.upper():
			linhas = replacer(linhas, letra, i)
			validaLetra = True
			acertos+=1
		i+=1
		
	print("A palavra é: ",linhas)
	if 	validaLetra:
		validaLetra = False
	else:
		erros+=1
		print("Você errou pela ",erros ," vez.")
		
	if acertos == len(palavras[x]):
		print("Você acertou tudo!. Fim de Jogo!")
		print("A palavra era: ", palavras[x])
		completou=True
	if erros == 6:
		print("Fim de Jogo!")
		completou = True