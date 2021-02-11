from google.colab import output
from IPython.display import clear_output
class Televisao:
    def __init__(self):
        self.volume = 0
        self.canal = 0
    def aumentarVolume(self):
        if self.volume == 100:
            print("Volume no Máximo")
        else:
            self.volume += 1
        
    def diminuirVolume(self):
        if self.volume == 0:
            print("Volume no Mínimo")
        else:
            self.volume -= 1
    def aumentarCanal(self):
        if self.canal == 100:
            print("Você chegou no último canal")
        else:
            self.canal += 1
    def diminuirCanal(self):
        if self.canal == 0:
            print("Você chegou no último canal")
        else:
            self.canal -= 1

def printTelevisao(canal,volume):
    print("*------------------------------------+---+--*")
    print("|                           Canal    |%3d|  |"%(canal))
    print("|                                    +---+  |")
    print("|                                           |")
    print("|                                           |")
    print("|                                           |")
    print("|                                           |")
    print("| +---+                                     |")
    print("| |%3d| Volume                              |"%(volume))
    print("*-+---+------------------------------M-^v-O-*")
    print("                 |       |")
    print("                 |       |")
    print("_________________|_______|__________________")

televisao = Televisao()
print("Ligando a TV .")
print("Ligando a TV ..")
print("Ligando a TV ...")
print("Ligando a TV ....")
while True:
    
    print("-------------------------------------------")
    printTelevisao(televisao.canal,televisao.volume)
    print("*---------------------*")
    print("| 1 - Aumenta volume  |")
    print("| 2 - Dimuinir volume |")
    print("| 3 - Avança Canal    |")
    print("| 4 - Voltar Canal    |")
    print("| 5 - Desligar TV     |")
    print("*---------------------*")
    opcao = int(input())
    clear_output()

    if opcao == 5:
      break
    elif opcao == 1:
      televisao.aumentarVolume()
    elif opcao == 2:
      televisao.diminuirVolume()
    elif opcao == 3:
      televisao.aumentarCanal()
    elif opcao == 4:
      televisao.diminuirCanal()
    else:
      print("*----------------*")
      print("| Opção invalida |")
      print("*----------------*")
print("TV desligada!!! (O.o)")
