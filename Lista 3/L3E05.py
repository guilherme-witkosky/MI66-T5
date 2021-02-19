#Altere o programa anterior permitindo ao usuário informar as populações e as 
#taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
#Exercicio
while True:
  a = int(input("Informe o total de Habitantes do paises A:"))
  porcentA = float(input("Informe a porcentagem de crescimento:"))
  b = int(input("Informe o total de Habitantes do paises B:"))
  porcentB = float(input("Informe a porcentagem de crescimento:"))
  anos = 0

  while True:
    if porcentA<porcentB and a<b :
      print("O pais A nunca chegará a ter mais habitantes que B")
      break;
    if a >= b:
      print("Demorou ", anos, "anos para A ter mais habitantes que B")
      print("A: %.0f" % a)
      print("B: %.0f" % b)
      break
    else:
      a = (a + ((porcentA * a ) / 100))
      b = (b + ((porcentB * b ) / 100))
      anos += 1
  s = input("Informe s para fecha o programa caso queira continuar aperte enter:")
  if s.lower()  == 's':
    break;
