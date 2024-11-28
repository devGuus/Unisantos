from genetica import *
import urllib.request

# Definir capacidade máxima da mochila
peso_maximo = 100  # Peso máximo permitido
capacidade_volume = 100  # Volume máximo permitido
categorias_obrigatorias = {"conforto"}  # Categorias essenciais para viabilidade

# Parâmetros do problema
n_de_cromossomos = 150
geracoes = 300

# Carregar itens do arquivo TXT
link_arquivo = "https://raw.githubusercontent.com/devGuus/Unisantos/refs/heads/main/Python/MochilaAcampamento/Roleta/itens_acampamento.txt"
itens_gerados = carregar_itens(link_arquivo)

n_de_itens = len(itens_gerados)

from matplotlib import pyplot as plt

# Função para calcular a média do fitness da população
def media_fitness(populacao, peso_maximo, capacidade_volume, itens):
    fitness_valores = [fitness(ind, peso_maximo, capacidade_volume, itens) for ind in populacao if fitness(ind, peso_maximo, capacidade_volume, itens) >= 0]
    return sum(fitness_valores) / len(fitness_valores) if fitness_valores else 0

# EXECUÇÃO DOS PROCEDIMENTOS
fitness_maximo = []
sucesso_rate = []

populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, peso_maximo, capacidade_volume, n_de_itens)]

for i in range(geracoes):
    populacao = evolve(populacao, peso_maximo, capacidade_volume, n_de_itens, n_de_cromossomos)

    # Adiciona o fitness médio da população à lista
    historico_de_fitness.append(media_fitness(populacao, peso_maximo, capacidade_volume, n_de_itens))

    # Fitness máximo da geração
    melhor_individuo = max(populacao, key=lambda x: fitness(x, peso_maximo, capacidade_volume, n_de_itens))
    fitness_maximo.append(fitness(melhor_individuo, peso_maximo, capacidade_volume, n_de_itens))

    # Calculando a taxa de sucesso (percentual de soluções viáveis)
    solucoes_viaveis = sum(1 for ind in populacao if fitness(ind, peso_maximo, capacidade_volume, n_de_itens) >= 0)
    sucesso_rate.append(solucoes_viaveis / len(populacao) * 100)

# PRINTS NO TERMINAL
# Exibindo a média de necessidade na mochila para cada geração e a melhor solução
print("\nEvolução das gerações:")
for indice, dados in enumerate(historico_de_fitness):
    # Melhor solução da geração
    melhor_solucao = max(populacao, key=lambda x: fitness(x, peso_maximo, capacidade_volume, n_de_itens))
    necessidade_melhor_solucao = fitness(melhor_solucao, peso_maximo, capacidade_volume, n_de_itens)
    print(f"Geração: {indice} | Média de necessidade na mochila: {dados:.2f} | Melhor solução: {necessidade_melhor_solucao}")

# Exibindo exemplos de boas soluções
print("\nExemplos de boas soluções:")
for i in range(5):
    individuo = populacao[i]
    necessidade_individuo = fitness(individuo, peso_maximo, capacidade_volume, n_de_itens)
    peso_total = sum(individuo[j] * n_de_itens[j]['peso'] for j in range(len(individuo)))
    print(f"Cromossomo: {individuo} | Necessidade total: {necessidade_individuo} | Peso total: {peso_total}g")

# GRÁFICOS
# Gráfico 1: Evolução do valor médio
plt.figure(figsize=(10, 5))
plt.plot(range(len(historico_de_fitness)), historico_de_fitness, label="Necessidade média", color="b")
plt.title("Problema da Mochila - Evolução da Necessidade Média")
plt.xlabel("Geração")
plt.ylabel("Necessidade Média")
plt.grid(True)
plt.legend()
plt.show()

# Gráfico 2: Fitness máximo por geração
plt.figure(figsize=(10, 5))
plt.plot(range(len(fitness_maximo)), fitness_maximo, label="Fitness máximo", color="g")
plt.title("Problema da Mochila - Fitness Máximo por Geração")
plt.xlabel("Geração")
plt.ylabel("Fitness Máximo")
plt.grid(True)
plt.legend()
plt.show()

# Gráfico 3: Taxa de sucesso por geração
plt.figure(figsize=(10, 5))
plt.plot(range(len(sucesso_rate)), sucesso_rate, label="Taxa de sucesso", color="r")
plt.title("Problema da Mochila - Taxa de Sucesso por Geração")
plt.xlabel("Geração")
plt.ylabel("Taxa de Sucesso (%)")
plt.grid(True)
plt.legend()
plt.show()

# Gráfico 4: Comparação do valor médio e fitness máximo por geração
plt.figure(figsize=(10, 5))
plt.plot(range(len(historico_de_fitness)), historico_de_fitness, label="Necessidade média", color="b")
plt.plot(range(len(fitness_maximo)), fitness_maximo, label="Fitness máximo", color="g", linestyle="--")
plt.title("Problema da Mochila - Comparação entre Necessidade Média e Fitness Máximo")
plt.xlabel("Geração")
plt.ylabel("Valor da Necessidade")
plt.legend()
plt.grid(True)
plt.show()
