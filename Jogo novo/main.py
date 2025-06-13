import classes



def jogar():
    jogador1 = classes.Cartas.sorteio_cartas()
    



if __name__ == "__main__":
    pessoa1 = input("Digite o nome do player 1: ")
    pessoa2 = input("Digite o nome do player 2: ")
    
    jogador1 = classes.Personagem(pessoa1, 100)
    jogador2 = classes.Personagem(pessoa2, 100)

    #jogador1.exibir()
    #jogador2.exibir()
    
    sorte1 = jogador1.jogar_dados()
    sorte2 = jogador2.jogar_dados()
    
    while True:
        if sorte1 > sorte2:
            print ("\nO player 1 irá começar a partida")
            break
        elif sorte2 > sorte1:
            print ("\nO player 2 ira comecar a partida")
            break
        else:
            print ("Empate, jogando dados novamente!\n")
            sorte1 = jogador1.jogar_dados()
            sorte2 = jogador2.jogar_dados()
    
    jogar1 = jogar()
    
    

    
    
            

            

    
    
    
