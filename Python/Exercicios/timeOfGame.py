a, b, c, d = list(map(int, input().split("Digite o horario de inicio e termino do jogo Exp( hr min hr min )")))
startHor = int(a)
startMin = int(b)
lastHor = int(c)
lastMin = int(d)
if (lastHor-startHor) > 0: #Horas
    hors = lastHor-startHor
else:
    hors = 24+(lastHor - startHor)
if (lastMin - startMin) < 0: #minutos
    mins = 60 + (lastMin - startMin)
    hors -= 1
else:
    mins = (lastMin - startMin)

print(f"O JOGO DUROU {hors} HORA(S) E {mins} MINUTO(s)")
