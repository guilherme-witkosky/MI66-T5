#Exercício 10
from random import randint
d = 0
def JogarCraps():
  d = randint(2,13)
  if d == 7 or d == 11:
   print('VOCÊ É UM GANHADOR NATURAL! ARRASOU!', d)
  elif d == 2 or d == 3 or d == 12:
   print('CRAPS! INFELIZMENTE VOCÊ PERDEU!', d)
  elif d in range(4,6) or d in range(8,10):
   print('SEU NÚMERO É: ', d)
   x = 0
   while d != x:
    print('DIGITE 0 PARA LANÇAR O DADO:')
    res = input()
    if res == '0':
     x = randint(2,13)
     print('SEU NÚMERO FOI: ', x)
     if x == 7:
      print('VOCÊ PERDEU!')
      break
    if  x != 7:
     print('VOCÊ GANHOU!')
     break
JogarCraps()