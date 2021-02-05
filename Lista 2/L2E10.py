#Exercício 10
print("Informe o período em que você estuda:")
print("(M) Matutino")
print("(V) Vespertino")
print("(N) Noturno")
print("------------------------------------------")
p = input("Seu Período = ")
print("------------------------------------------")
periodo = p.upper()
print("==========================================")
if periodo == "M":
  print("Bom Dia!")
  print("==========================================")
elif periodo == "V":
  print("Boa Tarde!")
  print("==========================================")
elif periodo == "N":
  print("Boa Noite!")
  print("==========================================")
else:
  print("Valor Inválido!")
  print("==========================================")
