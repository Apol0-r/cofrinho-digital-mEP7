def notasValidas(n,notas = [], i = 0):

    if i < n:
        notas += [int(input())] #lista que registra as notas
        return notasValidas(n,notas, i+1)
    
    return notas

def depositos(n,notas, carteiraDigital,i = 0,f = 0, r = 0):
   
    if r == 2 or r == 0:
        i = int(input()) #ele que comandará a recursão da função

    if i < 0:
        return carteiraDigital
    
    if f < len(notas):

        if i == notas[f]:
            carteiraDigital[f] += 1

        return depositos(n,notas,carteiraDigital,i,f +1, r = 1)
    
    return depositos(n, notas, carteiraDigital,i, f = 0, r = 2)

def saldo(n,notas, carteiraDigital, saldoD = 0, i = 0):
    if i < n:
        saldoD += notas[i] * carteiraDigital[i]
        return saldo(n,notas,carteiraDigital, saldoD, i+1)
    
    return saldoD

def estoqueN(n, notas, carteiraD, i = 0):
    if i < n:
        print(f"${notas[i]}: {carteiraD[i]}")
        return estoqueN(n,notas,carteiraD, i + 1)

def printSaldoEstoque(n,notas,listaSE, i = 0):
    if i < len(listaSE):
        if listaSE[i][0] == "s":
            print(f"Saldo: ${listaSE[i][1]}")
        else:
            estoqueN(n,notas,listaSE[i][1])

        return printSaldoEstoque(n,notas,listaSE, i + 1)
    
def menu(n,notas,carteiraD=0, saldoD=0, listaSaldEst = [],tuplaE = ()):
    
    if saldoD == 0:
        carteiraD = [0]*len(notas)

    opcao = input()

    if opcao == "DEPOSITO":
        carteiraD = depositos(n,notas,carteiraD)
        saldoD = saldo(n,notas,carteiraD)
        carteiraD2 = carteiraD + []
        tuplaE = ("e",carteiraD2)
    
    if opcao == "SALDO":

        listaSaldEst += [("s",saldoD)]
    
    if opcao == "ESTOQUENOTAS":
        listaSaldEst += [tuplaE]

    if opcao == "FIM":
        printSaldoEstoque(n,notas,listaSaldEst)
        return None

    return menu(n, notas, carteiraD, saldoD,listaSaldEst,tuplaE)
    
def main():
    n = int(input()) #representa o número de notas válidas do sistema
    notas = notasValidas(n)

    menu(n,notas)
   
main()