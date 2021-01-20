#Nome: Leonardo Willers Alves Pinto
#TIA:  41949420
matriz=[] 

######criando a matriz#########
def initialize():
    for i in range (0,3):
        linha=[]
        for j in range (0,3):
            linha.append("#")

        matriz.append(linha)
    

####### Mostrando a matriz na tela #############
def Print(matriz):
    for j in range(0,len(matriz)):
        print("   ", j, end="")
    print('')
    for i in range (0,len(matriz)):
        print(i, matriz[i])

###### função step ########
def step(matriz,lin,col,gamer):
    Booleano = False
    if matriz[lin][col] != "X" and matriz[lin][col] != "O":        
        matriz[lin][col]=gamer
        Print(matriz)
        Booleano = True
    else:
        print("Posição ja ocupada, não é possível inserir!!")
        while matriz[lin][col] == "X" or matriz[lin][col] == "O":
            lin=int(input("insira o valor da linha: "))
            col=int(input("insira o valor coluna: "))
        matriz[lin][col]=gamer
        Print(matriz)
        Booleano = True
    return Booleano,matriz
    

def status(matriz):
    verifi=False
    #verificar linhas###
    for i in range(0,len(matriz)):
        for j in range (0,1):
            if (matriz[i][j] == matriz[i][j+1] and matriz[i][j] == matriz[i][j+2]) and matriz[i][j] != "#":
                print(f"JOGADOR {matriz[i][j]} GANHOU !! JOGO FINALIZADO!!")
                verifi=True

    ##verificar colunas###
    for j in range (0,len(matriz)):
        for i in range (0,1):
            if (matriz[i][j] == matriz[i+1][j] and matriz[i][j] == matriz[i+2][j]) and matriz[i][j] != "#":
                print(f"JOGADOR {matriz[i][j]} GANHOU !! JOGO FINALIZADO!!")
                verifi=True

    ##verificar diagonal direita##
    for i in range(0,1):
        for j in range(0,1):
            if (matriz[i][j] == matriz[i+1][j+1] and matriz[i+1][j+1] == matriz[i+2][j+2]) and  matriz[i][j] != "#":
                print(f"JOGADOR {matriz[i][j]} GANHOU !! JOGO FINALIZADO!!")
                verifi=True

    ##verificar diagonal esquerda###
    for i in range(0,1):
        for j in range(0,1):
            if (matriz[i][j+2] == matriz[i+1][j+1] and matriz[i+1][j+1] == matriz[i+2][j]) and  matriz[i][j+2] != "#":
                print(f"JOGADOR {matriz[i][j+2]} GANHOU !! JOGO FINALIZADO!!")
                verifi=True

    return verifi

def main():
    
    #criando matriz#
    initialize()
    #printando matriz#
    Print(matriz)
    veri=status(matriz)
    cont=1
    while not(veri):
        print("\n")
        #PAR jogador X#
        if cont%2 == 0 :
            print("jogada do X")
            lin=int(input("insira o valor da linha (0 a 2): "))
            while lin <0 or lin >2:
                lin=int(input("VALOR INCORRETO!! insira o valor da linha (0 a 2): "))
            
            col=int(input("insira o valor coluna (0 a 2): "))
            while col <0 or col >2:
                col=int(input("VALOR INCORRETO!! insira o valor da coluna (0 a 2): "))
            
            step(matriz,lin,col,"X")
            veri=status(matriz)    

         #IMPAR jogador 0#
        if cont%2 == 1 :
            print("jogada do O")
            lin=int(input("insira o valor da linha (0 a 2): "))
            while lin <0 or lin >2:
                lin=int(input("VALOR INCORRETO!! insira o valor da linha (0 a 2): "))
            col=int(input("insira o valor coluna (0 a 2): "))
            while col <0 or col >2:
                col=int(input("VALOR INCORRETO!! insira o valor da coluna (0 a 2): "))
            step(matriz,lin,col,"O")
            veri=status(matriz) 

        cont=cont+1

main()