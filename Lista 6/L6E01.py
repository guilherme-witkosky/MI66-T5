#Exercício 1
palavra1 = input("Informe a 1ª Palavra: ")
palavra2 = input("Informe a 2ª Palavra: ")
print("=====================================================")
print("A 1ª PALAVRA FOI: ",palavra1)
print("ELA POSSUI ",len(palavra1)," CARACTERES")
print("-----------------------------------------------------")
print("A 2ª PALAVRA FOI: ",palavra2)
print("ELA POSSUI ",len(palavra2)," CARACTERES")
print("-----------------------------------------------------")
if palavra1 == palavra2:
  print("AS DUAS PALAVRAS TEM O MESMO CONTEÚDO")
else:
  print("AS DUAS PALAVRAS NÃO TEM O MESMO CONTEÚDO")
if len(palavra1) == len(palavra2):
  print("AS DUAS PALAVRAS TEM O MESMO TAMANHO")
else:
  print("AS DUAS PALAVRAS NÃO TEM O MESMO TAMANHO")
print("=====================================================")
