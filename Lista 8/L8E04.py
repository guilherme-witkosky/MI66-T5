class Pessoa:
    def __init__(self):
     self.nome = input("Informe o seu nome:")
     self.idade = int(input("Informe sua idade:"))
     self.peso = float(input("Informe seu peso:"))
     self.altura = float(input("Informe sua altura:"))
    def engordar():
        print("você tinha",self.peso)
        self.peso += 2
        print("Agora engordando você tem",self.peso)
    def emagrecer():
        print("você tinha",self.peso)
        self.peso -= 1.75
         print("Agora emagrecendo você tem",self.peso)
    def envelhecer():
        print("Você tinha",self.idade)
        self.idade += 1
        print("Agora envelhecendo você tem",self.idade)
    def crescer():
        print("Você tinha",self.altura)
        if(self.idade<21):
            self.altura += 0.5
        else:
            self.altura += 0.2
        print("Agora crescido você tem",self.altura)
p1 = Pessoa()
while True:
    print("*--------------------------------------*")
    print("|   Informe uma das opções abaixo:     |")
    print("*--------------------------------------*")
    print("| 1 - Engordar                         |")
    print("| 2 - Emagrecer                        |")
    print("| 3 - Crescer                          |")
    print("| 4 - Envelhecer                       |")
    print("| 5 - Sair                             |")
    print("*--------------------------------------*")
    opcao = input("")

    if int(opcao) ==5:
        break
    elif int(opcao) ==1:
        engordar()
    elif int(opcao) ==2:
        emagrecer()
    elif int(opcao) ==3:
        crescer()
    elif int(opcao) ==4:
        envelhecer()
    else:
        print("*--------------------------------------*")
        print("|           Opção inválida             |")
        print("*--------------------------------------*")
