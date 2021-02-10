fraseSeparadaInteira = []
fraseSeparada = ""
fraseInvertida = ""
frase = input("Digite a frase: ")

frase = ''.join(frase.split())

fraseSeparada = list(frase)

i = (len(fraseSeparada)-1)
while i >= 0:
	fraseInvertida += fraseSeparada[i]
	i-=1
	
print("Frase invertida: ",fraseInvertida)
print("Frase: ",fraseSeparada)
	
if frase.upper() == fraseInvertida.upper():
	print("É uma frase palíndromo")
else:
	print("Não é uma frase palíndromo")