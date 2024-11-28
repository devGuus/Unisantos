import numpy as np
import random

# Função que calcula o fitness (qualidade) de uma solução
def fitness(solucao, peso_maximo, pesos_e_valores):
    # Avalia a qualidade de uma solução.
    # Retorna o valor total da solução se ela respeitar o peso máximo permitido; 
    # caso contrário, retorna 0.
    peso_total, valor_total = 0, 0
    for i in range(len(solucao)):  
        if solucao[i]: #solucao (list): Lista binária indicando quais itens estão na mochila.
            peso_total += pesos_e_valores[i][0] # peso_total (int): Peso máximo permitido na mochila.
            valor_total += pesos_e_valores[i][1] # pesos_e_valores (list): Lista de pares [peso, valor] de cada item.
    return valor_total if peso_total <= peso_maximo else 0 # Valor total da solução (ou 0 se inválida).

# Função para construir uma solução baseada nos feromônios e heurísticas
def construir_solucao(pheromones, pesos_e_valores, peso_maximo, alpha=1, beta=2):
    """
    Args:
        pheromones (array): Array de feromônios para cada item.
        pesos_e_valores (list): Lista de pares [peso, valor] de cada item.
        peso_maximo (int): Peso máximo permitido na mochila.
        alpha (float): Importância dos feromônios.
        beta (float): Importância da heurística (valor/peso).

    Returns:
        list: Solução construída (lista binária indicando itens selecionados).
    """
    # Constrói uma solução para o problema da mochila utilizando feromônios e heurísticas
    solucao = np.zeros(len(pesos_e_valores), dtype=int)
    peso_atual = 0

    while peso_atual < peso_maximo:
        # Calcula probabilidades para cada item
        valores_heuristicos = [(pesos_e_valores[i][1] / pesos_e_valores[i][0]) ** beta 
                               if peso_atual + pesos_e_valores[i][0] <= peso_maximo and solucao[i] == 0
                               else 0
                               for i in range(len(pesos_e_valores))]
        probabilidades = pheromones ** alpha * valores_heuristicos
        soma_prob = sum(probabilidades)
        
        # Verifica se não há mais itens válidos
        if soma_prob == 0:
            break
        
        probabilidades = [p / soma_prob for p in probabilidades]
        
        # Escolhe o próximo item
        item = random.choices(range(len(pesos_e_valores)), weights=probabilidades, k=1)[0]
        solucao[item] = 1
        peso_atual += pesos_e_valores[item][0]
    
    return solucao

# Função para atualizar os feromônios com base nas soluções
def atualizar_feromonios(pheromones, todas_solucoes, fitness_values, evaporation_rate):
    """
    Atualiza os valores de feromônios com base nas soluções encontradas.

    Args:
        pheromones (array): Array de feromônios para cada item.
        todas_solucoes (list): Lista de soluções geradas na geração atual.
        fitness_values (list): Lista de valores de fitness correspondentes às soluções.
        evaporation_rate (float): Taxa de evaporação dos feromônios.

    Returns:
        None
    """
    pheromones *= (1 - evaporation_rate)  # Evaporação
    for solucao, valor in zip(todas_solucoes, fitness_values):
        if valor > 0:  # Considera apenas soluções válidas
            for i in range(len(solucao)):
                if solucao[i] == 1:
                    pheromones[i] += valor / 100  # Atualiza proporcional ao fitness
