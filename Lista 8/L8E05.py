#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
#A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
# com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, nrConta, nomeDono, saldo):
        self.nrConta = nrConta
        self.nomeDono = nomeDono
        self.saldo = saldo
    
    def saque(self, valorSaque):
        if valorSaque > self.saldo:
            print("Valor execede o saldo existente!")
        else:
            self.saldo -= valorSaque

    def verificarSaldo(self):
        print("Seu saldo é de: ", self.saldo)

    def verificarInfo(self):
        print("Seu nome é : ", self.nomeDono)

    def deposito(self, valorDep):
            self.saldo += valorDep
    
    def alterarNome(self, novoNome):
            if novoNome == "" or novoNome == " ":
                print("Caractere inválido")
            else:
                self.nomeDono = novoNome

conta01 = ContaCorrente(1,"Leonardo", 100)

conta01.saque(50)
conta01.deposito(1050)
conta01.alterarNome("Leonardo Pio")
conta01.verificarSaldo()
conta01.verificarInfo()


