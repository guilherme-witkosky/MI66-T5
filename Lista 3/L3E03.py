correto = 0
while True:
    nome = input("Informe seu nome:")
    idade = int(input("Informe sua idade:"))
    sal = float(input("Informe o seu salário:"))
    sexo = input("Informe F-Feminino ou M-Masculino para o sexo:")
    estado_civil= input("Informe o seu Estado Civil S-Soleteiro(a), C-Casado(a), V-Viuva(o) ou D-Divorciado(a):")
    if len(nome) <= 3:
        print("Nome inválido!!")
    else:
        correto += 1
    if idade <= 0 or idade >=150:
        print("Idade inválida!!")
    else:
        correto += 1
    if sal <=0:
        print("Salário inválido")
    else:
        correto += 1
    if sexo.upper() == "M" or sexo.upper() == "F":
        correto += 1
    else:
        print("Sexo inválido")
    if estado_civil.upper() == "S" or estado_civil.upper() == "C" or \
    estado_civil.upper() == "V" or estado_civil.upper() == "D" :
        correto += 1
    else:
        print("Estado Civil invállido")

    if correto == 5:
        print("----------------------------------------------")
        print("Nome informado foi:",nome)
        print("A idade:",idade)
        print("O seu salário:",sal)
        print("O sexo informado foi:", sexo )
        print("O estado civil selecionado foi:",estado_civil)
        print("----------------------------------------------")
        print("Programa Encerrado")
        break
    else:
        correto = 0
        print("--------------------------------")
        print("Informe os dados novamente")
    

 
