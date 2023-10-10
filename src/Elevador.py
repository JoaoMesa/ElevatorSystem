class Elevador:
    andar = 0
    direcao = 0
    alvo = 0
    
    def __init__(self):
        pass

    def converteDirecao(self):
      strdirecao = "parado"
      if self.direcao == 1:
        strdirecao = "subindo"
      elif self.direcao == -1:
        strdirecao = "descendo"
      return strdirecao

    def info(self):
        print(f" =============================== \nElevador no andar {self.andar}, está {self.converteDirecao()}, indo para {self.alvo}\n ===============================\n")
    
    def mudaAlvo(self, novoAndar):
        self.alvo = novoAndar
        if self.alvo != self.andar:
          self.direcao = self.alvo - self.andar
          self.direcao /= self.direcao
        self.info()

    def mudaAndar(self):
      if self.alvo != self.andar:
        self.andar += self.direcao
      else:
        self.direcao = 0
      self.info()
