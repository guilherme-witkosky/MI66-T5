#Exercício 25

sim = 0

print("===============================================")
print("INTERROGATÓRIO")
print("-----------------------------------------------")
print("1) Telefonou para a vítima?")
resp1 = input("(S) Sim   /   (N) Não      ")
r1 = resp1.upper()
if r1 == "S":
  sim = sim + 1
print("-----------------------------------------------")
print("2) Esteve no local do crime?")
resp2 = input("(S) Sim   /   (N) Não      ")
r2 = resp2.upper()
if r2 == "S":
  sim = sim + 1
print("-----------------------------------------------")
print("3) Mora perto da vítima?")
resp3 = input("(S) Sim   /   (N) Não      ")
r3 = resp3.upper()
if r3 == "S":
  sim = sim + 1
print("------------------------------------------------")
print("4) Devia para a vítima?")
resp4 = input("(S) Sim   /   (N) Não      ")
r4 = resp4.upper()
if r4 == "S":
  sim = sim + 1
print("------------------------------------------------")
print("5) Já trabalhou com a vítima?")
resp5 = input("(S) Sim   /   (N) Não      ")
r5 = resp5.upper()
if r5 == "S":
  sim = sim + 1
print("================================================")
if sim == 2:
  print("Conclusão: SUSPEITA")
elif sim >= 3 and sim <=4:
  print("Conclusão: CÚMPLICE")
elif sim >= 5:
  print("Conclusão: ASSASSINO")
else:
  print("Conclusão: INOCENTE")
print("================================================")
