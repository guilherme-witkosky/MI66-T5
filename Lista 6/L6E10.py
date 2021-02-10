#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
#Exercicio 10
def exe10t(num):
    if len(num) == 2 or len(num) == 1 and int(num)/10 <2:
        if int(num) == 0:
            print("Zero")
        elif int(num) == 1:
            print("Um")

        elif int(num) == 2:
            print("Dois")

        elif int(num) == 3:
            print("Tres")

        elif int(num) == 4:
            print("Quatro")

        elif int(num) == 5:
            print("Cinco")

        elif int(num) == 6:
            print("Seis")

        elif int(num) == 7:
            print("Sete")

        elif int(num) == 8:
            print("Oito")

        elif int(num) == 9:
            print("Nove")

        elif int(num) == 10:
            print("Dez")

        elif int(num) == 11:
            print("Onze")

        elif int(num) == 12:
            print("Doze")

        elif int(num) == 13:
            print("Treze")

        elif int(num) == 14:
            print("Quatorze")

        elif int(num) == 15:
            print("Quinze")

        elif int(num) == 16:
            print("Dezesseis")

        elif int(num) == 17:
            print("Dezessete")

        elif int(num) == 18:
            print("Dezoito")

        elif int(num) == 19:
            print("Dezenove") 

    if len(num) == 2 and int(num[0]) >= 2 :
 
        if int(num[0])== 2 and int(num[1]) > 0:
            print("Vinte e", num1(num))
        elif int(num) == 20:
            print("Vinte")

        elif int(num[0]) == 3 and int(num[1]) > 0:
            print("Trinta e", num1(num))

        elif int(num) == 30:
            print("Trinta")

        elif int(num[0]) == 4 and int(num[1]) > 0:
            print("Quarenta e", num1(num))

        elif int(num) == 40:
            print("Quarenta")

        elif int(num[0]) == 5 and int(num[1]) > 0:
            print("Cinquenta e", num1(num))

        elif int(num) == 50:
            print("Cinquenta")

        elif int(num[0]) == 6 and int(num[1]) > 0:
            print("Sessenta e", num1(num))

        elif int(num) == 60:
            print("Sessenta")

        elif int(num[0]) == 7 and int(num[1]) > 0:
            print("Setenta e", num1(num))

        elif int(num) == 70:
            print("Setenta")

        elif int(num[0]) == 8 and int(num[1]) > 0:
            print("Oitenta e", num1(num))

        elif int(num) == 80:
            print("Oitenta")

        elif int(num[0]) == 9 and int(num[1]) > 0:
            print("Noventa e", num1(num))

        elif int(num) == 90:
            print("Noventa")
    elif int(num) > 99 or int(num) < 0:
        print("Numero invalido")
        exit()
    
def num1(num):
      if num[1] == '1':
          return "Um"

      elif num[1] == '2':
          return "Dois"

      elif num[1] == '3':
          return "Tres"

      elif num[1] == '4':
          return "Quatro" 

      elif int(num[1]) == 5:
          return "Cinco"

      elif num[1] == '6':
          return "Seis" 

      elif num[1] == '7':
          return "Sete"

      elif num[1] == '8':
          return "Oito"

      elif num[1] == '9':
          return "Nove"
          
num = input("Informe um valor de 0 a 99: ")
exe10t(num)
