#Exercício 15
print("    /\    ")
print("a  /  \  b")
print("  /____\  ")
print("    c     ")
a = float(input("Informe o tamanho da aresta A: "))
b = float(input("Informe o tamanho da aresta B: "))
c = float(input("Informe o tamanho da aresta C: "))
print("=================================================")
if (b-c) < a and a < (b+c) and (a-c) < b and b < (a+c) and (a-b) < c and c < (a+b):
  print("Os valores inseridos podem ser um triângulo.")
  if a == b or b == c or a == c:
    if a == c and a == b:
      print("Tipo do Triângulo: EQUILÁTERO.")
    elif a == c or c == b or a == b: 
      print("Tipo do Triângulo: ISÓSCELES.")
  else:
    print("Tipo do Triângulo: ESCALENO.")
else:
  print("Os valores inseridos NÃO podem ser um triângulo.")
print("==================================================")
