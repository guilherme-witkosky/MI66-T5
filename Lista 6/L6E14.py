def converter(frase):
    dicionario_1337 = {1:"4",2:"|3",3:"(",4:"|)",5:"3",6:"ph",7:"6",8:"#",9:"|",10:"_|",11:"|<",12:"|_",13:"|V|",14:"/\/",15:"0",16:"|D",17:"(,)",18:"|2",19:"$",20:"7",21:"|_|",22:"V",23:"W",24:"><",25:"`/",26:"2"}
    leet =""
    
    for x in range(len(frase)):
        if frase[x].lower() == "a" :
           leet += "" + dicionario_1337.get(1)
        elif frase[x].lower() == "b":
            leet += "" + dicionario_1337.get(2)
        elif frase[x].lower() == "c":
           leet += "" + dicionario_1337.get(3)
        elif frase[x].lower() == "d":
            leet += "" + dicionario_1337.get(4)
        elif frase[x].lower() == "e":
            leet += "" + dicionario_1337.get(5)
        elif frase[x].lower() == "f":
           leet += "" + dicionario_1337.get(6)
        elif frase[x].lower() == "g":
            leet += "" + dicionario_1337.get(7)
        elif frase[x].lower() == "h":
            leet += "" + dicionario_1337.get(8)
        elif frase[x].lower() == "i":
            leet += "" + dicionario_1337.get(9)
        elif frase[x].lower() == "j":
           leet += "" + dicionario_1337.get(10)
        elif frase[x].lower() == "k":
            leet += "" + dicionario_1337.get(11)
        elif frase[x].lower() == "l":
           leet += "" + dicionario_1337.get(12)
        elif frase[x].lower() == "m":
            leet += "" + dicionario_1337.get(13)
        elif frase[x].lower() == "n":
           leet += "" + dicionario_1337.get(14)
        elif frase[x].lower() == "o":
            leet += "" + dicionario_1337.get(15)
        elif frase[x].lower() == "p":
            leet += "" + dicionario_1337.get(16)
        elif frase[x].lower() == "q":
            leet += "" + dicionario_1337.get(17)
        elif frase[x].lower() == "r":
            leet += "" + dicionario_1337.get(18)
        elif frase[x].lower() == "s":
            leet += "" + dicionario_1337.get(19)
        elif frase[x].lower() == "t":
            leet += "" + dicionario_1337.get(20)
        elif frase[x].lower() == "u":
            leet += "" + dicionario_1337.get(21)
        elif frase[x].lower() == "v":
            leet += "" + dicionario_1337.get(22)
        elif frase[x].lower() == "w":
            leet += "" + dicionario_1337.get(23)
        elif frase[x].lower() == "x":
           leet += "" + dicionario_1337.get(24)
        elif frase[x].lower() == "y":
            leet += "" + dicionario_1337.get(25)
        elif frase[x].lower() == "z":
            leet += "" + dicionario_1337.get(26)
        elif frase[x].lower() == " " :
            leet += " "
        else:
            leet += "" + frase[x].lower()
    return leet

frase = input("informe um texto sem acentuação transformarei para gradia leet spreak:")
print("Convertendo o texto informada para o padrão leet: ",converter(frase))
       

    
