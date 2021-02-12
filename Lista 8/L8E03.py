#Classe Retangulo: Crie uma classe que modele um retangulo:

#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

#Exercicio 3

class retangulo():
  def __init__(self, a, b):
    self.ladoA = a
    self.ladoB = b

  def mudarLado(self, novoLadoA, novoLadoB):
    self.ladoA = novoLadoA
    self.ladoB = novoLadoB

  def valLado(self):
    return (self.a, self.b)

  def calcArea(self, a, b):
    self.ladoA = a
    self.ladoB = b
    return (a*b) 

  def calcPeri(self, a, b):
    self.ladoA = a
    self.ladoB = b
    return ((a+b) * 2)

comLo = float(input("Comprimento do local: "))
larLo = float(input("Largura do local: "))

comPi = float(input("Comprimento do piso: "))
larPi = float(input("Largura do piso: "))

local = retangulo(comLo, larLo)
piso = retangulo(comPi, larPi)

resultado = (local.calcArea(comLo, larLo) / piso.calcArea(comPi, larPi))
rodape = (local.calcArea(comLo, larLo) % piso.calcArea(comPi, larPi))

print("Vai ser preciso %d pisos + %d rodape" %(resultado, rodape)
