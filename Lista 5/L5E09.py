value = int(input("Informe um valor:"))
def reservo(value):
    rever = 0
    while value > 0:
        rever *=10
        rever += value % 10
        value//=10
    return rever
print("O reverso do valor informado é: ",reservo(value))
