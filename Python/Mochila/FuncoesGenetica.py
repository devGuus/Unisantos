from random import getrandbits, randint, random, choice

# Criando um membro da população
def individual(numero_itens):
    return [ getrandbits(1) for x in range(numero_itens) ]

# Criar uma população
def populacao(numero_individuos, numero_itens):
    return [ individual(numero_itens) for x in range(numero_individuos) ]

# Avaliação do individuo
def fitnees(individuo, peso_maximo, peso_valores):
    peso_total, valor_total = 0, 0
    for indice, valor in enumerate(individuo):
        peso_total += (individuo[indice] * peso_valores[indice[0]])
        valor_total += (individuo[indice] * peso_valores[indice][1])
