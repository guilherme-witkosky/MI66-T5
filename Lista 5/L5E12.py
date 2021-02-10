#Exercício 12
import random
def embaralhar(palavra):
  listEmbaralhado = random.sample(palavra, len(palavra))
  embaralhado = ''.join(listEmbaralhado)
  print(embaralhado.upper())
p = input("Informe uma palavra: ")
embaralhar(p)