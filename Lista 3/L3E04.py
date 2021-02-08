#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#Exercicio 4

a = 80000
b = 200000
anos = 0

while True:

  if a >= b:
    print("Demorou ", anos, "anos para A ter mais habitantes que B")
    print("A: %.0f" % a)
    print("B: %.0f" % b)
    break
  else:
    a = (a + ((3 * a ) / 100))
    b = (b + ((1.5 * b ) / 100))
    anos += 1
