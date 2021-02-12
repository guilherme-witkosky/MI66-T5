#Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) 
# que aumente o salário do funcionário em uma certa porcentagem.
#Exemplo de uso:
#  harry=funcionário("Harry",25000)
#  harry.aumentarSalario(10)

#Exercicio 14

class funcionario():
    def __init__(self, nome, salario, aumento): 
        self.nome = nome 
        self.salario = salario 
        self.aumento = aumento
    
    def getNome(self): 
        return self.nome 
    
    def getSalario(self): 
        return self.salario

    def aumento(self):
        return ((self.salario * aumento)/100)

nome = input("Informe seu nome: ")
salario = float(input("Informe seu salario: "))
aumento = float(input("Informe a porcentagem de aumento: "))
    
teste = funcionario(nome, salario, aumento)

print("Nome:", teste.getNome(), "| Salario:", teste.getSalario(), "| Salario com aumento: ", teste.aumento())
