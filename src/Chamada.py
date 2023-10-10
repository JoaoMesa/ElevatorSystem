class Chamada:
  def __init__(self, andar, direcao):
    self.andar = andar
    self.direcao = direcao

  def converte(self):
    strdirecao = ""
    if self.direcao == 1:
      strdirecao = "subir"
    elif self.direcao == -1:
      strdirecao = "descer"
    return strdirecao

  def info(self):
      print(f"=============================== \nNo andar {self.andar}, quer/está {self.converte()} \n ===============================\n")
