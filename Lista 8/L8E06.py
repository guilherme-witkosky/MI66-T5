class Televisao:
    def __init__(self)
        self.volume = 0
        self.canal = 0
    def aumentarVolume(self):
        if self.volume == 100
            print("Volume no Máximo")
        else:
            self.volume += 1
        
    def aumentarVolume(self):
        if self.volume == 0
            print("Volume no Mínimo")
        else:
            self.volume -= 1
    def aumentarCanal(self):
        if self.canal == 0
            print("Você chegou no último canal")
        else:
            self.canal += 1
    def diminuirCanal(self):
        if self.canal == 0
            print("Você chegou no último canal")
        else:
            self.canal -= 1

def printTelevisao(canal,volume):
    print("*------------------------------------+---+--*")
    print("|                                    |%3d|  |"%(canal))
    print("|                                    +---+  |")
    print("|                                           |")
    print("|                                           |")
    print("|                                           |")
    print("|                                           |")
    print("| +---+                                     |")
    print("| |%3d|                                     |"%(volume))
    print("*-+---+------------------------------M-^v-O-*")
    print("                 |       |")
    print("                 |       |")
    print("_________________|_______|__________________")

televisao = Televisao()
printTelevisao(televisao.aumentarCanal(),televisao.aumentarVolume())