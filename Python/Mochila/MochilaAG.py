"""O problema da mochila: um problema de otimização combinatória.
O nome dá-se devido ao modelo de uma situação em que é necessário
preencher uma mochila com objetos de diferentes pesos e valores.
O objetivo é que se preencha a mochila com o maior valor possível,
não ultrapassando o peso máximo."""

from genetica import *
                #[peso,valor]
pesos_e_valores = [
    [9.4, 57], [7.4, 94], [7.7, 59], [7.4, 83], [2.9, 82],
    [1.1, 91], [7.3, 42], [9.0, 84], [8.1, 85], [7.2, 18],
    [7.5, 94], [4.2, 18], [4.4, 31], [5.7, 27], [2.0, 31],
    [2.0, 42], [9.9, 58], [9.5, 57], [5.2, 55], [7.1, 97],
    [6.8, 79], [1.6, 10], [7.9, 34], [3.0, 100], [1.6, 98],
    [9.0, 45], [2.1, 19], [4.9, 77], [7.0, 56], [6.8, 25],
    [7.7, 60], [2.1, 22], [8.4, 84], [1.9, 89], [6.5, 12],
    [3.8, 46], [2.5, 20], [4.3, 85], [9.9, 42], [8.5, 94]
]
peso_maximo = 140
n_de_cromossomos = 150
geracoes = 80
n_de_itens = len(pesos_e_valores) #Analogo aos pesos e valores

# Caso use rdn
# pesos_e_valores = [[randint(1, 50), randint(10, 500)] for _ in range(10)]  # Gerar itens aleatórios
# peso_maximo = randint(50, 200)  # Peso máximo aleatório
# e fazer a importação 
# from random import randint, random

#EXECUCAO DOS PROCEDIMENTOS
fitness_maximo = []
sucesso_rate = []

populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, peso_maximo, pesos_e_valores)]
for i in range(geracoes):
    populacao = evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos)
    
    # Adiciona o fitness médio da população à lista
    historico_de_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))

    # Fitness máximo da geração
    melhor_individuo = max(populacao, key=lambda x: fitness(x, peso_maximo, pesos_e_valores))
    fitness_maximo.append(fitness(melhor_individuo, peso_maximo, pesos_e_valores))
    
    # Calculando a taxa de sucesso (percentual de soluções viáveis)
    solucoes_viaveis = sum(1 for ind in populacao if fitness(ind, peso_maximo, pesos_e_valores) >= 0)
    sucesso_rate.append(solucoes_viaveis / len(populacao) * 100)

# PRINTS NO TERMINAL
# Exibindo a média de valor na mochila para cada geração e a melhor solução
for indice, dados in enumerate(historico_de_fitness):
    # Melhor solução da geração (maior valor)
    melhor_solucao = max(populacao, key=lambda x: fitness(x, peso_maximo, pesos_e_valores))
    valor_melhor_solucao = fitness(melhor_solucao, peso_maximo, pesos_e_valores)
    print(f"Geracao: {indice} | Média de valor na mochila: {dados} | Melhor solução: {valor_melhor_solucao} R$")

# Exibindo o peso máximo e os itens disponíveis com informações adicionais
print("\nPeso máximo:", peso_maximo, "g\n")
print("Itens disponíveis:")
for indice, i in enumerate(pesos_e_valores):
    peso, valor = i
    densidade = valor / peso  # Relação valor/peso
    print(f"Item {indice + 1}: {peso}g | R$ {valor}")

# Exibindo exemplos de boas soluções
print("\nExemplos de boas soluções:")
for i in range(5):
    individuo = populacao[i]
    valor_individuo = fitness(individuo, peso_maximo, pesos_e_valores)
    print(f"Cromossomo: {individuo} | Valor: R$ {valor_individuo} | Peso total: {sum(individuo[i] * pesos_e_valores[i][0] for i in range(len(individuo)))} g")

#GERADOR DE GRAFICO
from matplotlib import pyplot as plt
plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da mochila")
plt.xlabel("Geracao")
plt.ylabel("Valor medio da mochila")
plt.show()

# Gráfico 2: Fitness máximo por geração
plt.figure(figsize=(10, 5))
plt.plot(range(len(fitness_maximo)), fitness_maximo, label="Fitness máximo", color="g")
plt.title("Problema da Mochila - Fitness máximo por Geração")
plt.xlabel("Geração")
plt.ylabel("Fitness máximo")
plt.grid(True)
plt.legend()
plt.show()

# Gráfico 3: Taxa de sucesso por geração
plt.figure(figsize=(10, 5))
plt.plot(range(len(sucesso_rate)), sucesso_rate, label="Taxa de sucesso", color="r")
plt.title("Problema da Mochila - Taxa de Sucesso por Geração")
plt.xlabel("Geração")
plt.ylabel("Taxa de sucesso (%)")
plt.grid(True)
plt.legend()
plt.show()

# Gráfico 4: Comparação do valor médio e fitness máximo por geração
plt.figure(figsize=(10, 5))
plt.plot(range(len(historico_de_fitness)), historico_de_fitness, label="Valor médio", color="b")
plt.plot(range(len(fitness_maximo)), fitness_maximo, label="Fitness máximo", color="g", linestyle="--")
plt.title("Problema da Mochila - Comparação entre Valor Médio e Fitness Máximo")
plt.xlabel("Geração")
plt.ylabel("Valor da Mochila")
plt.legend()
plt.grid(True)
plt.show()