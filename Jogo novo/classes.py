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
    
    def exibir(self):
        return print(f"o personagem é {self.nome}")
    
    def jogar_dados(self):
        self.sorteado = random.randint(1,6)
        self.exibir_dados()
        return self.sorteado
    
    def exibir_dados(self):
        return print (f"{self.nome} tirou {self.sorteado} nos dados")
    
class Carta:
    
    def __init__(self,nome,energia_gasta,descricao):
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao
    
    def usar(self):
        pass
    
class CartaAumento (Carta):
    
    def __init__(self,nome: str ,energia_gasta: int, descricao: str,qual_aumento,aumento):
        super().__init__(energia_gasta,nome,descricao)
        self.qual_aumento = qual_aumento
        self.aumento = aumento
            
            
    
    def usar(self, beneficiario: Personagem):
        
        #vida maxima
        if self.qual_aumento == 1:
            beneficiario.vida_maxima += 20
            beneficiario.energia -= 1
        
        #aumento dano
        elif self.qual_aumento == 2:
            beneficiario.pontos_ataque += 15
            beneficiario.energia += 1
        
        #aumento energia max
        elif self.qual_aumento == 3:
            beneficiario.energia_maxima += 3
            beneficiario.energia -= 1     
        
        #aumento defesa
        elif self.qual_aumento == 4:
            beneficiario.pontos_defesa += 20
            beneficiario.energia -= 1
    

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
         
        

        
            
            
        
        
        
        
        