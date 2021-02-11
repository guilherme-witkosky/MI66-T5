class Bola:
    def __init__(self, cor, circu, material):
        self.cor=cor
        self.circu = circu
        self.material = material

    def trocarCor(self,cor):
        self.cor = cor
        print("A cor da bola foi alterado")

    def mostrarCor(self):
        print("A cor da bola é ",self.cor)


b1 = Bola((input("Informe a cor da bola:")),(float(input("Informe a circuferencia da bola:"))),(input("Informe o material da bola")))
b1.mostrarCor()
b1.trocarCor((input("informe a nova cor:")))
b1.mostrarCor()