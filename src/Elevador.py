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
          if self.alvo>self.andar:
            self.direcao = 1
          else:
            self.direcao = -1
        elif self.alvo == self.andar:
          self.direcao = 0
        

    def mudaAndar(self):
      while self.alvo != self.andar:
        self.andar += self.direcao
        self.info()
      self.direcao = 0
      
