import random
import os
import time

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Personagem:
    def __init__(self, nome, vida_atual):
        self.nome = nome
        self.vida_maxima = 100
        self.vida_atual = vida_atual
        self.pontos_ataque = 10
        self.pontos_defesa = 0
        self.energia = 1
        self.energia_maxima = 5
        self.mao_carta = []
    
    def construtor_maocarta(self):
        return f"{self.mao_carta}"
    
    def jogar_dados(self):
        self.sorteado = random.randint(1,6)
        self.exibir_dados()
        
        
        return self.sorteado
    
    def exibir_dados(self):
        return print (f"{self.nome} tirou {self.sorteado} nos dados")
    
    
    
class Partida ():
    def __init__(self, jogador1: Personagem, jogador2: Personagem):
        self.player1 = jogador1
        self.player2 = jogador2
        self.jogador_atual = jogador1
        self.oponente = jogador2
        
        
    def exibir(self):
        return print(f"jogador1 = {self.player1.nome}\njogador2 = {self.player2.nome}")
    
    
    def sorteio_cartas(self, x = None):

        if x == None:
            for i in range(4):
                numero_sorteado = random.randint(1,5)
                

                if numero_sorteado == 1:
                    carta1 = CartaAumento("Aumento", 2, "Aumenta algum atributo aleatório")
                    self.player1.mao_carta.append(carta1)
                    
                        
                elif numero_sorteado == 2:
                    carta2 = CartaAtordoamento("Atordoamento", 6, "Atordoa toda energia do inimigo")
                    self.player1.mao_carta.append(carta2)
                    
                elif numero_sorteado == 3:
                    carta3 = CartaCura("Cura dos anjos", 2, "Cura uma parte de sua vida")
                    self.player1.mao_carta.append(carta3)
                    
                elif numero_sorteado == 4:
                    carta4 = CartaDano("Dano", 1, "Causa dano baseado no ataque")
                    self.player1.mao_carta.append(carta4)
                    
                elif numero_sorteado == 5:
                    carta5 = CartaRoubo("Carta ladrona", 3, "Rouba uma carta aleatoria do inimigo")
                    self.player1.mao_carta.append(carta5)
                
                
            for i in range (4):

                numero_sorteado2 = random.randint(1,5)

                if numero_sorteado2 == 1:
                    carta6 = CartaAumento("Aumento", 2, "Aumenta algum atributo aleatório")
                    self.player2.mao_carta.append(carta6)
                    
                        
                elif numero_sorteado2 == 2:
                    carta7 = CartaAtordoamento("Atordoamento", 6, "Atordoa toda energia do inimigo")
                    self.player2.mao_carta.append(carta7)
                    
                elif numero_sorteado2 == 3:
                    carta8 = CartaCura("Cura dos anjos", 2, "Cura uma parte de sua vida")
                    self.player2.mao_carta.append(carta8)
                    
                elif numero_sorteado2 == 4:
                    carta9 = CartaDano("Dano", 1, "Causa dano baseado no ataque")
                    self.player2.mao_carta.append(carta9)
                    
                elif numero_sorteado2 == 5:
                    carta10 = CartaRoubo("Carta ladrona", 3, "Rouba uma carta aleatoria do inimigo")
                    self.player2.mao_carta.append(carta10)
            
        
    def exibir_mao(self):
        time.sleep(3)
        return print(f"\n\nCartas do {self.player1.nome}(jogador 1):\n\n{self.player1.mao_carta}\n\nCartas do {self.player2.nome}(jogador 2):\n\n {self.player2.mao_carta}\n\n")
    
    def exibir_infos1(self):
        print(f"           🌟{self.player1.nome}🌟         \n")
        print(f"            Vida: {self.player1.vida_atual}/{self.player1.vida_maxima}")
        print(f"            Escudo: {self.player1.pontos_defesa}")
        print(f"            Ataque: {self.player1.pontos_ataque}")
        print(f"            Energia: {self.player1.energia}/{self.player1.energia_maxima}\n\n")
    
    def exibir_infos2(self):
        print(f"           🌟{self.player2.nome}🌟         \n")
        print(f"            Vida: {self.player2.vida_atual}/{self.player2.vida_maxima}")
        print(f"            Escudo: {self.player2.pontos_defesa}")
        print(f"            Ataque: {self.player2.pontos_ataque}")
        print(f"            Energia: {self.player2.energia}/{self.player2.energia_maxima}\n\n")
    
    def sortear_uma_carta(self):
        numero_sorteado = random.randint(1,5)

        if numero_sorteado == 1:
            carta1 = CartaAumento("Aumento", 2, "Aumenta algum atributo aleatório")
            self.player1.mao_carta.append(carta1)
                    
                        
        elif numero_sorteado == 2:
            carta2 = CartaAtordoamento("Atordoamento", 6, "Atordoa toda energia do inimigo")
            self.player1.mao_carta.append(carta2)
                    
        elif numero_sorteado == 3:
            carta3 = CartaCura("Cura dos anjos", 2, "Cura uma parte de sua vida")
            self.player1.mao_carta.append(carta3)
                    
        elif numero_sorteado == 4:
            carta4 = CartaDano("Dano", 1, "Causa dano baseado no ataque")
            self.player1.mao_carta.append(carta4)
                    
        elif numero_sorteado == 5:
            carta5 = CartaRoubo("Carta ladrona", 3, "Rouba uma carta aleatoria do inimigo")
            self.player1.mao_carta.append(carta5)
    
    def construtor_de_cartas(self,carta):

        if carta[1] == "Atordoamento":
            CartaAtordoamento.usar(self.oponente,self.jogador_atual)


    def trocar_turno (self,numero):
        
        if numero == 1:
            self.jogador_atual = self.player2
            self.oponente = self.player1
        else:
            self.jogador_atual = self.player1
            self.oponente = self.player2
        
        
    def rolar_partida(self):

        
        print("Digite:\n1 - para usar carta\n2 - para comprar carta\n3 - para dançar")
        opcao = int(input("opcao = "))

        if opcao == 1:
            for i in range(len(self.jogador_atual.mao_carta)):
                print(f"{i+1} - {self.jogador_atual.mao_carta[i]}")

            indice = int(input("Número da carta que deseja usar: ")) - 1

            
            carta_escolhida = self.jogador_atual.mao_carta[indice]
            carta_escolhida.usar(self.jogador_atual, self.oponente)
            print(f"Você escolheu: {carta_escolhida}")
            
            
                      
            
            # elif opcao == 2:
            #     self.sortear_uma_carta()
            #     print(f"{self.jogador_atual.mao_carta}")
            #     break
            # else:
            #     print("\n\nvoce dançou\n\n")
            #     break
                
            # self.exibir_infos2()
        
        
            
    
    
    
    
    
class Carta:
    
    def __init__(self,nome,energia_gasta,descricao):
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao

    def __repr__(self):
        return f"{self.nome} - {self.descricao} (Custo: {self.energia_gasta})\n"
    
    def usar(self):
        pass
    
    def construtor_energia_gasta(self):
        return self.energia_gasta
    
class CartaAumento (Carta):
    
    def __init__(self,nome: str ,energia_gasta: int, descricao: str):
        super().__init__(nome,energia_gasta,descricao)
        self.qual_aumento = random.randint(1,4)
    
    
        
            
    def usar(self, beneficiario: Personagem):
        
        #vida maxima
        if self.qual_aumento == 1:
            beneficiario.vida_maxima += 20
            beneficiario.energia -= 1
            self.nome = "Carta Aumento Maximo"
            self.descricao = "Aumenta a quantidade de vida maxima"
            
        
        #aumento dano
        elif self.qual_aumento == 2:
            beneficiario.pontos_ataque += 15
            beneficiario.energia -= 1
            self.nome = "Anjo Da Destruicao"
            self.descricao = "aumenta o seu dano de ataque"
        
        #aumento energia max
        elif self.qual_aumento == 3:
            beneficiario.energia_maxima += 3
            beneficiario.energia -= 1
            self.nome = "MAAAAAAAAAX EEEENERGY"
            self.descricao = "aumenta a sua energia maxima"     
        
        #aumento defesa
        elif self.qual_aumento == 4:
            beneficiario.pontos_defesa += 20
            beneficiario.energia -= 1
            self.nome = "Escudo Dos Deuses"
            self.descricao = "Aumenta a sua defesa"
    



class CartaRoubo (Carta):
    def __init__(self,nome: str,energia_gasta: int,descricao : str):
        super().__init__(nome,energia_gasta,descricao)
        
    def usar(self, ladrao : Personagem, vitima : Personagem):
        sorteio = random.randint(0,len (vitima.mao_carta)-1)
        
        carta_roubada = vitima.mao_carta.pop(sorteio)
        ladrao.mao_carta.append(carta_roubada)
        
        return print ("Carta roubada com êxito")



class CartaAtordoamento (Carta):
    def __init__(self,nome: str, energia_gasta: int, descricao: str):
        super().__init__(nome,energia_gasta,descricao)
        
    def usar(self, atordoado : Personagem, atordoante : Personagem):
        atordoado.energia = 0
        #atordoante.energia -= atordoante.energia_maxima / 2
        
        return print ("Jogador atordoado com sucesso!")



class CartaDano (Carta):
    def __init__(self, nome: str, energia_gasta: int, descricao: str):
        super().__init__(nome,energia_gasta,descricao)
        
    def usar(self, vitima: Personagem, causador: Personagem):
        if vitima.pontos_defesa == 0:
            vitima.vida_atual -= causador.pontos_ataque
            
        elif vitima.pontos_defesa < causador.pontos_ataque:
            dano = causador.pontos_ataque - vitima.pontos_defesa
            vitima.pontos_defesa = 0
            vitima.vida_atual -= dano
            
        else:
            vitima.pontos_defesa -= causador.pontos_ataque
            
        causador.energia -= 1


    
class CartaCura(Carta):
    def __init__(self, nome: str, energia_gasta: int, descricao: str):
        super().__init__(nome,energia_gasta,descricao)
        
    def usar (self, beneficiario: Personagem):
        beneficiario.vida_atual += beneficiario.vida_maxima * 0.20       
        
        