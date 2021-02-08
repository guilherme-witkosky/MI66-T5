#Exercício 13
base = float(input("Informe o número que será a Base: "))
expoente = int(input("Informe o número que será o Expoente: "))
potencia = 1.0
i = 1.0
while i <= expoente:
  potencia = potencia * base
  i += 1
print("================================================================")
print(base," ELEVADO A ", expoente," É IGUAL A ",potencia)
print("================================================================")