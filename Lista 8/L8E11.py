from google.colab import output
from IPython.display import clear_output 

class CarroCarro: 

  def __init__(self, kmLitro, tanque):
    self.kmLitro = kmLitro
    self.tanque = tanque
  def andar(self, km):
    self.tanque = self.tanque - (km/self.kmLitro)
    print("====================================================")
    print("VOCÊ ANDOU: ",km," Km(s)")
    print("====================================================")
  def obterTanque(self):
    print("====================================================")
    print("TANQUE ATUAL DO VEÍCULO: %.2f L" % self.tanque)
    print("====================================================")
  def adicionarGasolina(self, qntd):
    self.tanque = self.tanque + qntd
    print("====================================================")
    print(qntd,"L FORAM ADICIONADOS AO TANQUE")
    print("====================================================")

  start = True
  while start == True:
    print("====================================================")
    print("INFORME A OPÇÃO QUE DESEJA: ")
    print("1 --> ADICIONAR VEÍCULO")
    print("2 --> ANDAR")
    print("3 --> OBSERVAR O TANQUE")
    print("4 --> ABASTECER")
    print("0 --> SAIR")
    print("----------------------------------------------------")
    res = int(input("Opção: "))
    if res == 0:
      clear_output()
      start = False
    elif res == 1:
      clear_output()
      print("QUANTOS Km(s) O VEÍCULO FAZ POR LITRO?")
      kml = float(input("Km/L: "))
      print("QUANTOS LITROS DE GASOLINA O VEÍCULO POSSUI AGORA?")
      gas = float(input("Litros: "))
      __init__(CarroCarro, kml, gas)
    elif res == 2:
      clear_output()
      print("QUANTOS Km(s) O VEÍCULO SE DESLOCOU?")
      km = float(input("Km(s): "))
      andar(CarroCarro, km)
    elif res == 3:
      clear_output()
      obterTanque(CarroCarro)
    elif res == 4:
      clear_output()
      print("QUANTOS LITROS DESEJA ABASTECER?")
      litro = float(input("Litros: "))
      adicionarGasolina(CarroCarro, litro)
    else:
      clear_output()
      print("====================================================")
      print("RESPOSTA INVÁLIDA!")
      print("====================================================")
