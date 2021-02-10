import re

numero = ""

numero = input("Informe seu telefone: ")

if len(numero) > 7:
  if re.search('\\-\\b', numero, re.IGNORECASE):
    numero = numero.split("-")
    numero = numero[0]+numero[1]
    if len(numero) == 7:
      numero = "3"+numero

print(numero)