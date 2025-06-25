import classes
import os


def jogar(pessoa1,pessoa2):
    
    Partida = classes.Partida(pessoa1,pessoa2)
    #exibir = Partida.exibir()
    sorteio1 = Partida.sorteio_cartas()
    sorteio2 = Partida.sorteio_cartas()
    exibir_mao = Partida.exibir_mao()
    #exibir_info1 = Partida.exibir_infos1()
    #exibir_info2 = Partida.exibir_infos2()
    rolar_partida = Partida.rolar_partida()
    



if __name__ == "__main__":
    pessoa1 = input("Digite o nome do player 1: ")
    pessoa2 = input("Digite o nome do player 2: ")
    print ("\n\n")
    
    jogador1 = classes.Personagem(pessoa1, 100)
    jogador2 = classes.Personagem(pessoa2, 100)

    #jogador1.exibir()
    #jogador2.exibir()
    
    sorte1 = jogador1.jogar_dados()
    sorte2 = jogador2.jogar_dados()
    
    while True:
        if sorte1 > sorte2:
            os.system("cls")
            print ("\n      O player 1 irá começar a partida        ")
            começar = jogar(jogador1,jogador2)
            break
        elif sorte2 > sorte1:
            print ("\n      O player 2 ira comecar a partida        ")
            começar = jogar(jogador2,jogador1)
            break
        else:
            print ("Empate, jogando dados novamente!\n")
            sorte1 = jogador1.jogar_dados()
            sorte2 = jogador2.jogar_dados()
    
    
    
    
    
    

    
    
            

            

    
    
    
