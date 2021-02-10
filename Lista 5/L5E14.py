#Exercício 14
def gerarCombos(lista, n):    
  for i in lista:
    for j in lista:            
      if n + i + j == 15 and (n != i and n != j and i != j):
        combinacoes.append((n, i, j))

def gerarQuadrado(combo, L1):
  linha1 = L1    
  for i in range(len(combo)):
    linha2 = combo[i]
    for j in range(len(combo)):
      linha3 = combo[j]        
      if (linha1[0] + linha2[0] + linha3[0] == 15) and\
               (linha1[1] + linha2[1] + linha3[1] == 15) and\
               (linha1[2] + linha2[2] + linha3[2] == 15) and\
               (linha1[0] + linha2[1] + linha3[2] == 15) and\
               (linha1[2] + linha2[1] + linha3[0] == 15):     

                if (linha1[0] not in linha2) and\
                   (linha1[1] not in linha2) and\
                   (linha1[2] not in linha2):

                    print(linha1)
                    print(linha2)
                    print(linha3)
                    print()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinacoes = []

for n in range(1,10):    
  gerarCombos(lista, n)

print()

for x in combinacoes:
  gerarQuadrado(combinacoes, x)