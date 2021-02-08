#Exercício 16
ultimo=0
penultimo=1
termo = 0
print("=========================================")
while termo < 500:
  print(termo)
  print("=========================================")
  termo = ultimo + penultimo
  penultimo = ultimo
  ultimo = termo