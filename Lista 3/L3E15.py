#Exercício 15
n = int(input("QUE TERMO DESEJA ENCONTRAR: "))
ultimo=1
penultimo=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print("=========================================")
    print(termo)
    print("=========================================")