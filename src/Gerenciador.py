from Elevador import Elevador
from Chamada import Chamada

class Gerenciador:

  def __init__(self):
      self.limiteinf = int(input("Qual o menor andar do edifício?"))
      self.limitesup = int(input("Qual o maior andar do edifício?"))
      self.e1 = Elevador()
      self.filaDeChamadas = []
      self.run()


  def run(self):
    while True:
      self.e1.info()
      escolha = int(input("O que deseja fazer?\n 0 - Sair \n 1 - Chamar elevador \n 2 - Esperar \n"))

      if escolha == 0:
        break

      if escolha == 1:
        ch = Chamada(int(input("Qual andar você está?\n")))
        if ch.andar == self.e1.andar:
          ch = Chamada(int(input("Pra onde você quer ir?\n")))
        if ch.andar >= self.limiteinf and ch.andar <= self.limitesup:
          self.filaDeChamadas.append(ch)
        else:
          print("=============================== \n CHAMADA INVÁLIDA \n ===============================\n")

      if self.e1.alvo == self.e1.andar and len(self.filaDeChamadas) > 0:
        temp = self.filaDeChamadas[0].andar
        self.e1.mudaAlvo(temp)

      self.e1.mudaAndar()

      j = 0
      for i in self.filaDeChamadas:
        if i.andar == self.e1.andar:
          self.filaDeChamadas.pop(j)
          print(f" =============================== \nCHAMADA CUMPRIDA NO ANDAR {i.andar}\n ===============================\n")
        j+=1



