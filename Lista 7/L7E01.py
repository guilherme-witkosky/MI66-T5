readTe = open('ip.txt','r')
listaInvalido = []
listaValido = []
def printIp(list):
    for x in range(len(list)):
        print(list[x])
def validacao():
    for linha in readTe:
        IP = linha.split()
        def isIPv4(s):
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False
        def isIPv6(s):
            if len(s) > 4:
                return False
            try : return int(s, 16) >= 0 and s[0] != '-'
            except:
                return False
        if IP[0].count(".") == 3 and all(isIPv4(i) for i in IP[0].split(".")):
            listaValido.append(IP[0])
        else:
            listaInvalido.append(IP[0])
validacao()
print("======================================================================")
print("ENDEREÇOS VÁLIDOS:")
printIp(listaValido)
print("----------------------------------------------------------------------")
print("ENDEREÇOS INVÁLIDOS:")
printIp(listaInvalido)
print("======================================================================")


    
