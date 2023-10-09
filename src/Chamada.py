class Chamada:
  def __init__(self, andar, direcao):
    self.andar = andar
    self.direcao = direcao

  def converte(self):
    strdirecao = "parado"
    if self.direcao == 1:
      strdirecao = "subindo"
    elif self.direcao == -1:
      strdirecao = "descendo"
    return strdirecao

  def info(self):
      print(f"No andar {self.andar}, está {self.converte()}")
