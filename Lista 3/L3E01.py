#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
#Exercico 1

while True:
    nota = float(input("Informe uma nota de 0 a 10: "))
    if nota >= 0 and nota <= 10:
      print(nota)
      break
    else: 
      print("Nota invalida")
