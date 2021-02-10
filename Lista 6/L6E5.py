#Exercício 5
nome = input("INSIRA SEU NOME: ").upper()
for i in range(len(nome), 0, -1):
  print(nome[:i])