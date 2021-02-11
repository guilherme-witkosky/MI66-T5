from google.colab import output
from IPython.display import clear_output 
class bombaCombustivel: 

  def __init__(self, tipoCombustivel, valorLitro, qntdCombustivel):
    self.tipoCombustivel = tipoCombustivel
    self.valorLitro = valorLitro
    self.qntdCombustivel = qntdCombustivel

  def getTipoCombustivel(self):
    return self.tipoCombustivel

  def getValorCombustivel(self):
    return self.valorCombustivel

  def getQntdCombustivel(self):
    return self.qntdCombustivel

  def abastecePorValor(self, valorAbastecido):
    qntdAbastecida = (valorAbastecido/self.valorLitro)
    self.qntdCombustivel = self.qntdCombustivel - qntdAbastecida
    print("=============================================================")
    print("O VEÍCULO FOI ABASTECIDO COM %.2f LITROS" % qntdAbastecida)
    print("=============================================================")

  def abastecePorLitro(self, qntdAbastecida):
    valorAbastecido = qntdAbastecida * self.valorLitro
    self.qntdCombustivel = self.qntdCombustivel - qntdAbastecida
    print("=============================================================")
    print("TOTAL A PAGAR: R$ %.2f" % valorAbastecido)
    print("=============================================================")
  
  def setValorLitro(self, valorLitro):
    self.valorLitro = valorLitro
    print("=============================================================")
    print("NOVO VALOR DO COMBUSTÍVEL = R$ %.3f" % self.valorLitro)
    print("=============================================================")
  
  def setTipoCombustivel(self, tipoCombustivel):
    self.tipoCombustivel = tipoCombustivel
    print("=============================================================")
    print("COMBUSTÍVEL NA BOMBA AGORA: ", self.TipoCombustivel)
    print("=============================================================")

  def setQntdCombustivel(self, qntdCombustivel):
    self.qntdCombustivel = qntdCombustivel
    print("=============================================================")
    print("QUANTIDADE DE COMBUSTÍVEL NA BOMBA: ", self.qntdCombustivel)
    print("=============================================================")

  def listarCombustivel(self):
    print("=============================================================")
    print("Combustível: ",self.tipoCombustivel)
    valor = float(self.valorLitro)
    print("Valor do Litro: R$ %.2f" % valor)
    print("Combustível Restante: %.2f Litros" % self.qntdCombustivel)
    print("=============================================================")
  start = True

  while start == True:
    print("========================================================")
    print("O INSIRA O QUE DESEJA FAZER: ")
    print("1 --> Abastecer Por Litro")
    print("2 --> Abastecer Por Valor")
    print("3 --> Alterar Bomba")
    print("4 --> Listar Informações da Bomba")
    print("")
    print("0 --> SAIR")
    print("========================================================")
    resp = int(input("Opção: "))
    if resp == 0:
      clear_output()
      print("========================================================")
      print("PROGRAMA FOI ENCERRADO!")
      print("========================================================")
      start = False
    elif resp == 1:
      clear_output()
      print("========================================================")
      print("INFORME QUANTOS LITROS DESEJA ABASTECER")
      qntdAbastecida = float(input("LITROS: "))
      abastecePorLitro(bombaCombustivel, qntdAbastecida)
    elif resp == 2:
      clear_output()
      print("========================================================")
      print("INFORME O VALOR QUE DESEJA ABASTECER")
      valorAbastecido = float(input("R$: "))
      abastecePorValor(bombaCombustivel, valorAbastecido)
    elif resp == 3:
      clear_output()
      print("========================================================")
      print("O INSIRA O QUE DESEJA FAZER: ")
      print("1 --> Mudar Combustível")
      print("2 --> Mudar Valor do Litro")
      print("3 --> Mudar Quantidade Restante")
      print("4 --> Mudar Tudo")

      print("0 --> VOLTAR")
      print("========================================================")
      opc = int(input("Opção: "))
      if opc == 0:
        clear_output()
        start = True
      elif opc == 1:
        clear_output()
        print("========================================================")
        print("INFORME O NOVO COMBUSTÍVEL: ")
        comb = input("COMBUSTÍVEL: ")
        setTipoCombustivel(bombaCombustivel, comb)
      elif opc == 2:
        clear_output()
        print("=============================================================")
        print("INFORME O NOVO VALOR DO LITRO")
        valor = float(input("R$: "))
        setValorLitro(bombaCombustivel, valor)
      elif opc == 3:
        clear_output()
        print("=============================================================")
        print("INFORME A QUANTIDADE RESTANTE")
        qntd = float(input("LITROS: "))
        setQntdCombustivel(bombaCombustivel, qntd)
      elif opc == 4:
        clear_output()
        print("=============================================================")
        print("INFORME O COMBUSTÍVEL: ")
        comb = input("COMBUSTÍVEL: ")
        print("INFORME O VALOR DO LITRO")
        valor = float(input("R$: "))
        print("INFORME A QUANTIDADE")
        qntd = float(input("LITROS: "))
        __init__(bombaCombustivel, comb, valor, qntd)
        print("=============================================================")
      else:
        clear_output()
        print("=============================================================")
        print("RESPOSTA INVÁLIDA")
        start = True
    elif resp == 4:
      clear_output()
      listarCombustivel(bombaCombustivel)
    else:
      clear_output()
      print("=============================================================")
      print("RESPOSTA INVÁLIDA")
      start = True