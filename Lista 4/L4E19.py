#Exercício 19
i=True
votoWin = 0
votoUnix = 0
votoLinux = 0
votoNet = 0
votoMac = 0
votoOutro = 0
votoInvalido = 0
while i:
  print("Qual o Melhor Sistema Operacional Para Uso em Servidores?")
  print("1 -- Windows Server")
  print("2 -- Unix")
  print("3 -- Linux")
  print("4 -- Netware")
  print("5 -- MacOS")
  print("6 -- Outro")
  print("")
  print("0 -- Encerrar a Votação")
  print("")
  voto = int(input("-->"))
  if voto == 1:
    votoWin += 1
  elif voto == 2:
    votoUnix += 1
  elif voto == 3:
    votoLinux += 1
  elif voto == 4:
    votoNet += 1
  elif voto == 5:
    votoMac += 1
  elif voto == 6:
    votoOutro += 1
  elif voto == 0:
    i=False
  else:
    print("+------------------------------------------------------------------------------------+")
    print("|                     VOTO INVÁLIDO, INFORME UM VALOR ENTRE 0-6                      |")
    print("+------------------------------------------------------------------------------------+")
    i=True
  opcoes= ["Windows Server","Unix","Linux","Netware","MacOS","Outro"]
  totalVotos = [votoWin,votoUnix,votoLinux,votoNet,votoMac,votoOutro]
  porcentagem = []
  for voto in totalVotos:
    porcent = (voto * 100)/sum(totalVotos)
    porcentagem.append(porcent)
print("===================================================================================================================================")
print("                                                               RESULTADO DA VOTAÇÃO                                                ")
print("-----------------------------------------------------------------------------------------------------------------------------------")
x = 0
for opcao in opcoes:
  print(opcoes[x])
  print("TOTAL DE VOTOS = ",totalVotos[x])
  print("PORCENTAGEM DOS VOTOS %.2f = "%porcentagem[x])
  x+=1
  print("---------------------------------------------------------------------------------------------------------------------------------")
print("TOTAL DE VOTOS = ",sum(totalVotos))
print("-----------------------------------------------------------------------------------------------------------------------------------")
maximo = max(totalVotos)
t = 0
vencedor = 0
for opcao in totalVotos:
  if opcao == maximo:
    vencedor = t
  t+=1
print("O Vencedor da Votação Foi ",opcoes[vencedor],", Com ",totalVotos[vencedor]," Votos! ",porcentagem[vencedor],"% dos Votos Totais!")
print("====================================================================================================================================")