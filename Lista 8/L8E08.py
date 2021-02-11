#Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

#Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; 
#Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração,
# o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde,
# ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela 
# pode ser calculada a qualquer momento.

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