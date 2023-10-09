e1 = Elevador()
#e1.info()
#e1.mudarAndar(4)

c1 = Chamada(0, 1)
c2 = Chamada(1, 1)
c3 = Chamada(5, -1)
c4 = Chamada(12, -1)
#c1.info()

filaDeChamadas = []
filaDeChamadas.append(c1)
filaDeChamadas.append(c2)
filaDeChamadas.append(c3)
filaDeChamadas.append(c4)

for i in filaDeChamadas:
  i.info()
