#Exercício 15
i=True
notas=[]
listaReversa=[]
while i:
  num = float(input(print("Informe Sua Nota: ")))
  if num <= (-1):
    i=False
  else:
    notas.append(num)
qntNotas = len(notas)
somaNotas = sum(notas)
media = somaNotas/qntNotas
acimaMedia = 0
abaixoSete = 0
for notinha in notas:
  if notinha > media:
    acimaMedia+=1
  if notinha < 7:
    abaixoSete+=1
for i in reversed(notas):
    listaReversa.append(i)
print("========================================================================================================================================================")
print("Quantidade de Notas Informadas: ",qntNotas)
print("Ordem de Inserção: ",notas)
print("Ordem Inversa:", listaReversa)
print("Soma das Notas Informadas = ",somaNotas)
print("Média das Notas Informadas = %.2f" % media)
print("Quantidade de Notas Acima da Média: ", acimaMedia)
print("Quantidade de Notas Abaixo de Sete: ", abaixoSete)
print("")
print("Programa Foi Encerrado! Muito Obrigado Por Usar o Programa! Até Mais!")
print("========================================================================================================================================================")
