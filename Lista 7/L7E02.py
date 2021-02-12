arquivo2 = open('relatorio.txt','w')
arquivo = open('usuarios.txt','r')

totalidade = contador = 0
listagem = []
pessoas = []

def main(arquivo2):
    global totalidadeidade, listagem, pessoas

    converter()
    porcentagem = percentual()

    arquivo2.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    arquivo2.write('------------------------------------------------------------------------\n')
    arquivo2.write('Nr.  Usuário       Espaço utilizado     % do uso\n')
    arquivo2.write('\n')

    for i in range(contador):
        arquivo2.write('%i    %s%7.2fMB%19.2f%%'%(i+1, pessoas[i], listagem[i], porcentagem[i]))
        arquivo2.write('\n')

    media = totalidade/6
    espaço = (len('%.2f'%totalidade) - len('%.2f'%media))*' '
    arquivo2.write('\n')
    arquivo2.write('Espaço total ocupado: %.2fMB\n'%(totalidade))
    arquivo2.write('Espaço medio ocupado: %s%.2fMB'%(espaço ,media))

    arquivo2.close()


def converter():
    global listagem, pessoas, totalidade, contador

    while True:
        x = arquivo.readline()
        if x == '':
            break

        pessoas.append(x[:16])
        y = x[16:]
        listagem.append(int(y)/1048576)
        totalidade += int(y)
        contador += 1

    totalidade/= 1048576


def percentual():
    global totalidade, listagem
    porcentagem = []
    for i in range(contador):
        porcentagem.append(listagem[i]*100/totalidade)

    return porcentagem

main(arquivo2)
arquivo.close()