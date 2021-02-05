#Exercício 8
prodA = float(input("Informe o preço do Produto A: "))
prodB = float(input("Informe o preço do Produto B: "))
prodC = float(input("Informe o preço do Produto C: "))
print("=========================================================================")
print("Produto A = R$ %.2f" % round(prodA,2))
print("Produto B = R$ %.2f" % round(prodB,2))
print("Produto C = R$ %.2f" % round(prodC,2))
print("-------------------------------------------------------------------------")
if prodA < prodB and prodA < prodC:
  print("Você deve comprar o Produto A! Ele é o mais barato.")
elif prodB < prodA and prodB < prodC:
  print("Você deve comprar o Produto B! Ele é o mais barato.")
elif prodC < prodA and prodC < prodB:
  print("Você deve comprar o Produto C! Ele é o mais barato.")
elif prodA == prodB and prodA < prodC:
  print("Você deve comprar o Produto A ou Produto B! Eles são os mais baratos.")
elif prodA == prodC and prodA < prodB:
  print("Você deve comprar o Produto A ou Produto C! Eles são os mais baratos.")
elif prodB == prodC and prodB < prodA:
  print("Você deve comprar o Produto B ou Produto C! Eles são os mais baratos.")
elif prodA == prodB and prodA == prodC:
  print("Você pode comprar qualquer um dos produtos! Eles custam a mesma coisa.")
print("-------------------------------------------------------------------------")
print("=========================================================================")
