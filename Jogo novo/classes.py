import random

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
        
        
    def exibir(self):
        return print(f"jogador1 = {self.player1.nome}\njogador2 = {self.player2.nome}")
    
    
    def sorteio_cartas(self):
    
        for i in range(8):
            self.random = random.randint(1,5)
            
                
            if random == 1:
                carta1 = CartaAumento()
                self.player1.mao_carta.append[carta1]
                
                    
            elif random == 2:
                 carta2 = CartaAtordoamento()
                 self.player1.mao_carta.append[carta2]
                
            elif random == 3:
                 carta3 = CartaCura()
                 self.player1.mao_carta.append[carta3]
                
            elif random == 4:
                carta4 = CartaDano()
                self.player1.mao_carta.append[carta4]
                
            elif random == 5:
                 carta5 = CartaRoubo()
                 self.player1.mao_carta.append[carta5]
                 
        
                
                
        
        
        
        
    
    
    
    
    
    
    
    
class Carta:
    
    def __init__(self,nome,energia_gasta,descricao):
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao
    
    def usar(self):
        pass
    
class CartaAumento (Carta):
    
    def __init__(self,nome: str ,energia_gasta: int, descricao: str):
        super().__init__(energia_gasta,nome,descricao)
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
            beneficiario.energia += 1
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
        super().__init__(energia_gasta,nome,descricao)
        
    def usar(self, ladrao : Personagem, vitima : Personagem):
        sorteio = random.randint(0,len (vitima.mao_carta)-1)
        
        carta_roubada = vitima.mao_carta.pop(sorteio)
        ladrao.mao_carta.append(carta_roubada)
        
        return print ("Carta roubada com êxito")

class CartaAtordoamento (Carta):
    def __init__(self,nome: str, energia_gasta: int, descricao: str):
        super().__init__(nome,descricao,energia_gasta)
        
    def usar(self, atordoado : Personagem, atordoante : Personagem):
        atordoado.energia = 0
        atordoante.energia -= atordoante.energia_maxima / 2
        
        return print ("Jogador atordoado com sucesso!")

class CartaDano (Carta):
    def __init__(self, nome: str, energia_gasta: int, descricao: str):
        super().__init__(nome,descricao,energia_gasta)
        
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
         
        

        
            
            
        
        
        
        
        