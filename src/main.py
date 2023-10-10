filaDeChamadas = []
e1 = Elevador()

while True:
  e1.info()
  escolha = int(input("O que deseja fazer?\n 0 - Sair \n 1 - Chamar elevador \n"))

  if escolha == 0:
    for i in filaDeChamadas:
      i.info()
    break;

  if escolha == 1:
    andarCh = int(input("Qual andar?\n"))
    direcaoCh = int(input("Digite 1 para subir e -1 para descer\n"))
    novaChamada = Chamada(andarCh, direcaoCh)
    filaDeChamadas.append(novaChamada)

  
