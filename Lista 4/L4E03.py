#Exercício 3
i=1
notas=[]
while i<=4:
  num = float(input(print("Sua ",i,"ª Nota: ")))
  notas.append(num)
  i+=1
somaNotas = sum(notas)
qntNotas = len(notas)
media = somaNotas/qntNotas
i=1
print("==============================================================")
for notinha in notas:
  print("Sua ",i,"ª Nota Foi ",notinha)
  i+=1
print("--------------------------------------------------------------")
print("Sua Média é %.2f" % media)
print("==============================================================")
