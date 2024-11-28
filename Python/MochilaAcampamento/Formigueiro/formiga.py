import numpy as np
from matplotlib import pyplot as plt
from genetica import *

# Configuração inicial do problema
pesos_e_valores = [[4, 30], [8, 10], [8, 30], [25, 75], 
                   [2, 10], [50, 100], [6, 300], [12, 50], 
                   [100, 400], [8, 300]]
peso_maximo = 100
n_formigas = 50
n_geracoes = 80
n_itens = len(pesos_e_valores)

# Parâmetros ACO
evaporation_rate = 0.5  # Taxa de evaporação dos feromônios
alpha = 1  # Importância dos feromônios
beta = 2   # Importância da heurística
pheromones = np.ones((n_itens,))  # Inicialização uniforme dos feromônios

# Histórico para análise do desempenho
historico_de_fitness = []
melhor_solucao = None
melhor_valor = 0

# Execução do algoritmo de Colônia de Formigas
for geracao in range(n_geracoes):
    solucoes = []
    fitness_values = []
    
    # Cada formiga constrói uma solução
    for _ in range(n_formigas):
        solucao = construir_solucao(pheromones, pesos_e_valores, peso_maximo, alpha, beta)
        solucoes.append(solucao)
        valor = fitness(solucao, peso_maximo, pesos_e_valores)
        fitness_values.append(valor)
        
        # Atualiza o melhor global
        if valor > melhor_valor:
            melhor_valor = valor
            melhor_solucao = solucao
    
    # Atualiza feromônios
    atualizar_feromonios(pheromones, solucoes, fitness_values, evaporation_rate)
    
    # Armazena histórico
    media_fitness = np.mean(fitness_values)
    historico_de_fitness.append(media_fitness)

# Exibe os resultados
print(f"Melhor valor encontrado: {melhor_valor}")
print("Melhor solução:", melhor_solucao)

# Gráfico do histórico de fitness
plt.plot(range(n_geracoes), historico_de_fitness)
plt.title("Problema da Mochila - Colônia de Formigas")
plt.xlabel("Geração")
plt.ylabel("Fitness Médio")
plt.grid(True)
plt.show()
