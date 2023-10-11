e1 = Elevador()
filaDeChamadas = []


while True:
  e1.info()
  escolha = int(input("O que deseja fazer?\n 0 - Sair \n 1 - Chamar elevador \n 2 - Esperar \n"))

  if escolha == 0:
    break

  if escolha == 1:
    ch = Chamada(int(input("Qual andar?\n")))
    filaDeChamadas.append(ch)
  
  if e1.alvo == e1.andar and len(filaDeChamadas) > 0:
    temp = filaDeChamadas[0].andar
    e1.mudaAlvo(temp)

  e1.mudaAndar()
  if len(filaDeChamadas)> 0 and e1.andar == filaDeChamadas[0].andar: 
    filaDeChamadas.pop(0)
