#Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). 
# Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. 
# Escreva um pequeno programa que teste sua classe.

#Exercicio 13

class funcionario():
    def __init__(self, nome, salario): 
        self.nome = nome 
        self.salario = salario 
    
    def getNome(self): 
        return self.nome 
    
    def getSalario(self): 
        return self.salario

nome = input("Informe seu nome: ")
salario = float(input("Informe seu salario: "))
    
teste = funcionario(nome, salario)

print("Nome:", teste.getNome(), "| Salario:", teste.getSalario())
