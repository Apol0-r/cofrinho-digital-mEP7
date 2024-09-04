def notas(n, carteira = [], i = 0):
    if i < n:
        item = int(input())
        if item not in carteira:
            carteira += [item]
        
        return notas(n,carteira, i +1)

    return carteira



def deposito(notasV, carteiraD = []):
    
    if carteiraD == []:
        carteiraD = [0]*len(notasV)
        
    
    n = int(input())

    if n >= 0:
        if n in notasV:
            indice = notasV.index(n)
            carteiraD[indice] += 1

        return deposito(notasV,carteiraD)
    

    return carteiraD

def saldo(notasV,carteiraD,saldo_d = 0, i = 0):

    if i < len(notasV) and (len(notasV) == len(carteiraD)):

        saldo_d += notasV[i]*carteiraD[i]

        return saldo(notasV,carteiraD,saldo_d, i + 1)
    
    return saldo_d

def estoqueNotas(notasV,carteiraD, i = 0):
    
    if carteiraD == []:
        carteiraD = [0]*len(notasV)

    if i < len(notasV):

        nota = notasV[i]
        quantidade = carteiraD[i]

        print(f"${nota}: {quantidade}")
    
        return estoqueNotas(notasV,carteiraD, i + 1)
    
        
def impressao(comando,notasV,i = 0):
    if i < len(comando):

        if comando[i][0] == "s":
            saldo = comando[i][1]
            print(f"Saldo: ${saldo}")
        
        if comando[i][0] == "e":
            carteiradigital = comando[i][1]
            estoqueNotas(notasV,carteiradigital)
    
        return impressao(comando,notasV, i+1)



def menu(notasV,carteira_digital = [], saldo_digital = 0,comando_digital = []):

    opcao = input()


    if opcao == "DEPOSITO":
        carteira_digital = deposito(notasV,carteira_digital + [])
    
    if opcao == "SALDO":
        saldo_digital = saldo(notasV,carteira_digital)

        comando_digital += [("s",saldo_digital)] 
    
    if opcao == "ESTOQUENOTAS":
        comando_digital += [("e",carteira_digital)] + []
    
    if opcao == "FIM":
        impressao(comando_digital,notasV)
        return None

    
    return menu(notasV, carteira_digital,saldo_digital)

def main():

    numero_notas_validas = int(input())

    notas_validas = notas(numero_notas_validas)

    menu(notas_validas)


main()