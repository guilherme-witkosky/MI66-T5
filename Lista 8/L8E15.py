#Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique 
#quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
# Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = (fome+saude)/2
    
    def calcHumor(self):
        self.humor = (self.fome+self.saude)/2

    def alimentar(self, comida):
        if (self.fome + comida) > 100:
            self.fome += comida
            comida =  (self.fome % 100)
            self.fome -= comida
        else:
            self.fome += comida

        if (self.saude + 5) > 100:
            self.saude += 5
            x =  (self.saude % 100)
            self.saude -= x
        else:
            self.saude += 5

        self.calcHumor()
		
	def brincar(self):
		if (self.humor + 5) > 100:
            self.humor += 5
            x =  (self.humor % 100)
            self.humor -= x
        else:
            self.humor += 5


    def aniversario(self):
        self.idade +=1
        self.humor = 100

    def viver(self):
        self.fome -= 5
        if fome < 35:
            self.saude -= 5
        self.calcHumor()

    def status(self):
       print(self.nome)
       print("Saúde: ",self.saude)
       print("Fome: ",self.fome)
	   print("Humor: ",self.humor)
       print("Idade: ",self.idade)
            
jorge = BichinhoVirtual("Jorge",100,100,4)

i = 0
while i < 5:
    jorge.viver()
    i+=1

jorge.status()
jorge.alimentar(40)

i = 0
while i < 10:
    jorge.viver()
    i+=1

jorge.aniversario()
jorge.status()

i = 0
while i < 15:
    jorge.viver()
    i+=1
	
jorge.status()
jorge.brincar()
jorge.status()