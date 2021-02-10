#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
#taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
#que é o custo de um item antes do imposto. 
#A função “altera” o valor de custo para incluir o imposto sobre vendas

valorCusto = 0
taxa = 0
valorCusto = float(input("Informe valor de custo: "))
taxa = float(input("Informe valor da taxa: "))

def somaImposto(taxaImposto, custo):
	print("Valor sem imposto: ",custo)
	
	custo *= 1+(taxaImposto/100)
	
	print("Valor com imposto: ",custo)
	print("Taxa de imposto: ",taxaImposto,"%")
 
somaImposto(taxa,valorCusto)