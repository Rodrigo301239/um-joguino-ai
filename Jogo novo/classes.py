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
        self.energia = 3
        self.energia_maxima = 3
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
        self.contador = 0
        
        
    def exibir(self):
        return print(f"jogador1 = {self.player1.nome}\njogador2 = {self.player2.nome}")
    
    
    def sorteio_cartas(self, x = None):

        if x == None:
            for i in range(4):
                numero_sorteado = random.randint(1,20)
                

                if numero_sorteado == 1 or numero_sorteado == 6 or numero_sorteado == 11 or numero_sorteado == 15 or numero_sorteado == 20:
                    carta1 = CartaAumento("Aumento", 1, "Aumenta algum atributo aleatório")
                    self.player1.mao_carta.append(carta1)
                    
                        
                elif numero_sorteado == 2:
                    carta2 = CartaAtordoamento("Atordoamento", 1, "Atordoa toda energia do inimigo")
                    self.player1.mao_carta.append(carta2)
                    
                elif numero_sorteado == 3 or numero_sorteado == 8 or numero_sorteado == 12 or numero_sorteado == 16:
                    carta3 = CartaCura("Cura dos anjos", 1, "Cura uma parte de sua vida")
                    self.player1.mao_carta.append(carta3)
                    
                elif numero_sorteado == 4 or numero_sorteado == 9 or numero_sorteado == 13 or numero_sorteado == 17:
                    carta4 = CartaDano("Dano", 1, "Causa dano baseado no ataque")
                    self.player1.mao_carta.append(carta4)
                    
                elif numero_sorteado == 5 or numero_sorteado == 10 or numero_sorteado == 14:
                    carta5 = CartaRoubo("Carta ladrona", 1, "Rouba uma carta aleatoria do inimigo")
                    self.player1.mao_carta.append(carta5)
                
                elif numero_sorteado == 7 or numero_sorteado == 18:
                    carta11 = CartaCoringa("Carta coringa",1,"nao faz nada demais")
                    self.player1.mao_carta.append(carta11)

                elif numero_sorteado == 19:
                    carta12 = CartaEscudoDivino("Carta Escudo Divino", 1, "Da um escudo de 50 pontos para o usuario")
                    self.player1.mao_carta.append(carta12)


                
                numero_sorteado2 = random.randint(1,20)
                    

                if numero_sorteado2 == 1 or numero_sorteado2== 6 or numero_sorteado2 == 11 or numero_sorteado2== 15 or numero_sorteado2 == 20:
                    carta1 = CartaAumento("Aumento", 1, "Aumenta algum atributo aleatório")
                    self.player2.mao_carta.append(carta1)
                        
                            
                elif numero_sorteado2 == 2:
                    carta2 = CartaAtordoamento("Atordoamento", 1, "Atordoa toda energia do inimigo")
                    self.player2.mao_carta.append(carta2)
                        
                elif numero_sorteado2 == 3 or numero_sorteado2 == 8 or numero_sorteado2 == 12 or numero_sorteado2 == 16:
                    carta3 = CartaCura("Cura dos anjos", 1, "Cura uma parte de sua vida")
                    self.player2.mao_carta.append(carta3)
                        
                elif numero_sorteado2 == 4 or numero_sorteado2 == 9 or numero_sorteado2 == 13 or numero_sorteado2 == 17:
                    carta4 = CartaDano("Dano", 1, "Causa dano baseado no ataque")
                    self.player2.mao_carta.append(carta4)
                        
                elif numero_sorteado2== 5 or numero_sorteado2 == 10 or numero_sorteado2 == 14:
                    carta5 = CartaRoubo("Carta ladrona", 1, "Rouba uma carta aleatoria do inimigo")
                    self.player2.mao_carta.append(carta5)
                    
                elif numero_sorteado2 == 7 or numero_sorteado2 == 18:
                    carta11 = CartaCoringa("Carta coringa",1,"nao faz nada demais")
                    self.player2.mao_carta.append(carta11)

                elif numero_sorteado2 == 19:
                    carta12 = CartaEscudoDivino("Carta Escudo Divino", 1, "Da um escudo de 50 pontos para o usuario")
                    self.player2.mao_carta.append(carta12)
            
        
    def exibir_mao(self):
        time.sleep(3)
        return print(f"\n\nCartas do {self.player1.nome}(jogador 1):\n\n{self.player1.mao_carta}\n\nCartas do {self.player2.nome}(jogador 2):\n\n {self.player2.mao_carta}\n\n")
    
    def exibir_infos(self):

        print ("VOCE:\n")
        print(f"           🌟{self.jogador_atual.nome}🌟         \n")
        print(f"            Vida: {self.jogador_atual.vida_atual}/{self.jogador_atual.vida_maxima}")
        print(f"            Escudo: {self.jogador_atual.pontos_defesa}")
        print(f"            Ataque: {self.jogador_atual.pontos_ataque}")
        print(f"            Energia: {self.jogador_atual.energia}/{self.jogador_atual.energia_maxima}\n\n")

        print("OPONENTE:\n")
        print(f"           🌟{self.oponente.nome}🌟         \n")
        print(f"            Vida: {self.oponente.vida_atual}/{self.oponente.vida_maxima}")
        print(f"            Escudo: {self.oponente.pontos_defesa}")
        print(f"            Ataque: {self.oponente.pontos_ataque}")
        print(f"            Energia: {self.oponente.energia}/{self.oponente.energia_maxima}\n\n")
    
    def sortear_uma_carta(self):
        numero_sorteado = random.randint(1, 20)
        self.jogador_atual.energia -= 1

        if numero_sorteado in [1, 6, 11, 15, 20]:
            carta = CartaAumento("Aumento", 1, "Aumenta algum atributo aleatório")
        elif numero_sorteado == 2:
            carta = CartaAtordoamento("Atordoamento", 1, "Atordoa toda energia do inimigo")
        elif numero_sorteado in [3, 8, 12, 16]:
            carta = CartaCura("Cura dos anjos", 1, "Cura uma parte de sua vida")
        elif numero_sorteado in [4, 9, 13, 17]:
            carta = CartaDano("Dano", 1, "Causa dano baseado no ataque")
        elif numero_sorteado in [5, 10, 14]:
            carta = CartaRoubo("Carta ladrona", 1, "Rouba uma carta aleatória do inimigo")
        elif numero_sorteado in [7, 18]:
            carta = CartaCoringa("Carta coringa", 1, "Não faz nada demais")
        elif numero_sorteado == 19:
            carta = CartaEscudoDivino("Carta Escudo Divino", 1, "Dá um escudo de 50 pontos para o usuário")

        self.jogador_atual.mao_carta.append(carta)
        print(f"{self.jogador_atual.nome} comprou a carta: {carta.nome}")

    
            
    def trocar_turno (self):
        self.contador += 1
        resto = self.contador % 2
        
        if resto == 1:
            self.jogador_atual = self.player2
            self.oponente = self.player1
        else:
            self.jogador_atual = self.player1
            self.oponente = self.player2
        
        
    def rolar_partida(self):
        atordoado = 0
        for i in range(self.jogador_atual.energia_maxima):
            
            
            exibir_info = self.exibir_infos()
            
            print("Digite:\n1 - para usar carta\n2 - para comprar carta\n3 - para dançar")
            opcao = int(input("opcao = "))

            if opcao == 1:
                for i in range(len(self.jogador_atual.mao_carta)):
                    print(f"{i+1} - {self.jogador_atual.mao_carta[i]}")

                indice = int(input("Número da carta que deseja usar: ")) - 1

                
                carta_escolhida = self.jogador_atual.mao_carta[indice]
                print(f"Você escolheu: {carta_escolhida}")
                
                carta_escolhida.usar(self.jogador_atual, self.oponente)
                self.jogador_atual.mao_carta.pop(indice)
                
                if carta_escolhida.nome == "Atordoamento":
                    atordoado = 1

            elif opcao == 2:
                 self.sortear_uma_carta()
                 print("CARTA COMPRADA COM SUCESSO")
            
            elif opcao == 3:
                print ("\n\n\n\nDANCANDO\n\n\n")
                print (f"{self.jogador_atual.nome} dançou\n\n")
                
        if atordoado == 1:
            self.oponente.energia = 0
            self.jogador_atual.energia = self.jogador_atual.energia_maxima
            self.rolar_partida()
        else:
            self.jogador_atual.energia = self.jogador_atual.energia_maxima
            self.oponente.energia = self.oponente.energia_maxima
            self.trocar_turno()
            self.rolar_partida()

    
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
            
    def usar(self, beneficiario: Personagem, quem_usou: Personagem):
        
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
            beneficiario.energia_maxima += 1
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

        for i in range(len(vitima.mao_carta)):
            if vitima.mao_carta[i].nome == "Carta coringa":
                carta_roubada = vitima.mao_carta.pop(i)
                ladrao.mao_carta.append(carta_roubada)
                ladrao.energia -= 1
                return print (f"Carta Coringa roubada com êxito")


        sorteio = random.randint(0,len (vitima.mao_carta)-1)
        ladrao.energia -= 1
        
        carta_roubada = vitima.mao_carta.pop(sorteio)
        ladrao.mao_carta.append(carta_roubada)
        
        return print (f"Carta {vitima.mao_carta[sorteio].nome} roubada com êxito")



class CartaAtordoamento (Carta):
    def __init__(self,nome: str, energia_gasta: int, descricao: str):
        super().__init__(nome,energia_gasta,descricao)
        
    def usar(self, atordoante : Personagem ,atordoado : Personagem):
        atordoado.energia = 0
        atordoante.energia -= 1
        
        return print ("Jogador atordoado com sucesso!")



class CartaDano (Carta):
    def __init__(self, nome: str, energia_gasta: int, descricao: str):
        super().__init__(nome,energia_gasta,descricao)
        
    def usar(self, causador: Personagem,vitima: Personagem):
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
        
    def usar (self, beneficiario: Personagem,oponente: Personagem):
        
        if beneficiario.vida_atual < beneficiario.vida_maxima:
            beneficiario.vida_atual += beneficiario.vida_maxima * 0.20  
            beneficiario.energia -= 1
        else:
            beneficiario.energia -= 1
            pass

        if beneficiario.vida_atual > beneficiario.vida_maxima:
            beneficiario.vida_atual = beneficiario.vida_maxima  

class CartaCoringa (Carta):
    def __init__(self, nome: str, energia_gasta: int, descricao: str):
        super().__init__(nome,energia_gasta,descricao)
    
    def usar(personagem_atual: Personagem,oponente: Personagem):
        personagem_atual -= 1

class CartaEscudoDivino (Carta):
    def __init__(self, nome: str, energia_gasta: int, descricao: str):
        super().__init__(nome,energia_gasta,descricao)
    
    def usar (self, beneficiario: Personagem,oponente: Personagem):
        beneficiario.pontos_defesa += 50
        beneficiario.energia -= 1

class 
        


        
        

