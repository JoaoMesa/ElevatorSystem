class Elevador:
    andar = 0
    estado = 0
    direcao = 0
    
    def __init__(self):
        pass

    def info(self):
        print(f"Elevador no andar {self.andar}, andando: {self.estado}, com direção {self.direcao}")
    
    def mudarAndar(self, novoAndar):
        self.andar = novoAndar
        self.info()
