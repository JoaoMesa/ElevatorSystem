e1 = Elevador()

while True:
  e1.info()
  escolha = int(input("O que deseja fazer?\n 0 - Sair \n 1 - Chamar elevador \n 2 - Esperar \n"))

  if escolha == 1:
    ch = Chamada(int(input("Qual andar?\n")), int(input("Digite 1 para subir e -1 para descer\n")))
    e1.mudaAlvo(ch.andar)
  
  e1.mudaAndar()
