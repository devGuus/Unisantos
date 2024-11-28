from random import getrandbits, randint, random, choice
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# Função para gerar um indivíduo
def individual(n_de_itens):
    return [getrandbits(1) for _ in range(n_de_itens)]

# Função para gerar a população inicial
def population(n_de_individuos, n_de_itens):
    return [individual(n_de_itens) for _ in range(n_de_individuos)]

# Função de fitness
def fitness(individuo, peso_maximo, capacidade_volume, itens):
    peso_total, necessidade_total, volume_total = 0, 0, 0
    categorias_selecionadas = set()

    for indice, valor in enumerate(individuo):
        if valor == 1:  # Se o item foi selecionado
            item = itens[indice]
            peso_total += item["peso"]
            necessidade_total += item["necessidade"]
            volume_total += item["volume"]
            categorias_selecionadas.add(item["categoria"])

    # Penalizar se exceder peso ou volume máximo
    if peso_total > peso_maximo or volume_total > capacidade_volume:
        return -1

    # Penalizar se faltar categorias obrigatórias
    faltantes = categorias_obrigatorias - categorias_selecionadas
    if faltantes:
        necessidade_total -= 100 * len(faltantes)  # Penalidade por categoria ausente

    return max(necessidade_total, -1)  # Garantir que o fitness não seja negativo

# Função de seleção por roleta viciada
def selecao_roleta(pais):
    fitness_total = sum(f for f, _ in pais)
    if fitness_total == 0:
        return choice(pais)[1], choice(pais)[1]  # Escolher aleatoriamente se fitness total for 0

    def sortear():
        valor_sorteado = random() * fitness_total
        acumulado = 0
        for fitness, individuo in pais:
            acumulado += fitness
            if acumulado >= valor_sorteado:
                return individuo

    return sortear(), sortear()

# Função de evolução da população
def evolve(populacao, peso_maximo, capacidade_volume, itens, mutate=0.05):
    pais = [
        [fitness(ind, peso_maximo, capacidade_volume, itens), ind]
        for ind in populacao
        if fitness(ind, peso_maximo, capacidade_volume, itens) >= 0
    ]
    pais.sort(reverse=True)

    # Reprodução
    filhos = []
    while len(filhos) < len(populacao):
        pai, mae = selecao_roleta(pais)
        ponto_corte = randint(1, len(pai) - 1)
        filho = pai[:ponto_corte] + mae[ponto_corte:]
        filhos.append(filho)

    # Mutação
    for individuo in filhos:
        if mutate > random():
            pos_to_mutate = randint(0, len(individuo) - 1)
            individuo[pos_to_mutate] = 1 - individuo[pos_to_mutate]  # Troca entre 0 e 1

    return filhos

# Dados de itens para teste (substitua conforme necessário)
itens_gerados = [
    {"nome": f"Item {i+1}", "peso": randint(1, 15), "necessidade": randint(10, 100), "volume": randint(1, 10), "categoria": choice(["comida", "ferramenta", "roupa"])}
    for i in range(30)
]

# Parâmetros do problema
peso_maximo = 150
capacidade_volume = 120
categorias_obrigatorias = {"comida"}  # Categorias essenciais para viabilidade
n_de_cromossomos = 50
geracoes = 300
n_de_itens = 30

# Execução do algoritmo
populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [
    sum(fitness(ind, peso_maximo, capacidade_volume, itens_gerados) for ind in populacao if fitness(ind, peso_maximo, capacidade_volume, itens_gerados) >= 0) / len(populacao)
]

for _ in range(geracoes):
    populacao = evolve(populacao, peso_maximo, capacidade_volume, itens_gerados)
    media_fitness = sum(fitness(ind, peso_maximo, capacidade_volume, itens_gerados) for ind in populacao if fitness(ind, peso_maximo, capacidade_volume, itens_gerados) >= 0) / len(populacao)
    historico_de_fitness.append(media_fitness)

# Resultados
for indice, dados in enumerate(historico_de_fitness):
    print(f"Geração: {indice} | Necessidade média: {dados:.2f}")

# Melhor solução
melhor_solucao = max(populacao, key=lambda ind: fitness(ind, peso_maximo, capacidade_volume, itens_gerados))
print("\nMelhor solução encontrada:")
for indice, valor in enumerate(melhor_solucao):
    if valor == 1:
        item = itens_gerados[indice]
        print(f" - {item['nome']} | Peso: {item['peso']}g | Volume: {item['volume']}cm³ | Necessidade: {item['necessidade']} | Categoria: {item['categoria']}")

# Gráfico de evolução
plt.plot(historico_de_fitness)
plt.title("Evolução do Fitness Médio")
plt.xlabel("Gerações")
plt.ylabel("Fitness Médio")
plt.grid(True)
plt.show()

melhor_fitness_por_geracao = []
for _ in range(geracoes):
    populacao = evolve(populacao, peso_maximo, capacidade_volume, itens_gerados)
    media_fitness = sum(fitness(ind, peso_maximo, capacidade_volume, itens_gerados) for ind in populacao if fitness(ind, peso_maximo, capacidade_volume, itens_gerados) >= 0) / len(populacao)
    melhor_fitness = max(fitness(ind, peso_maximo, capacidade_volume, itens_gerados) for ind in populacao)
    historico_de_fitness.append(media_fitness)
    melhor_fitness_por_geracao.append(melhor_fitness)

# Gráfico do Melhor Fitness por Geração
plt.figure(figsize=(10, 5))
plt.plot(melhor_fitness_por_geracao, label="Melhor Fitness", color="green")
plt.title("Melhoria do Melhor Fitness ao Longo das Gerações")
plt.xlabel("Gerações")
plt.ylabel("Melhor Fitness")
plt.legend()
plt.grid(True)
plt.show()

def calcular_diversidade(populacao):
    """Calcula a diversidade da população como a média de genes iguais."""
    n_genes = len(populacao[0])  # Número de genes por indivíduo
    diversidade = 0

    for gene in range(n_genes):
        # Conta quantos indivíduos têm 1 no gene atual
        soma_gene = sum(individuo[gene] for individuo in populacao)
        proporcao = soma_gene / len(populacao)
        diversidade += proporcao * (1 - proporcao)  # Variância binomial

    return diversidade / n_genes  # Média da variância por gene

# No loop principal, calcule a diversidade:
diversidade_por_geracao = []
for _ in range(geracoes):
    populacao = evolve(populacao, peso_maximo, capacidade_volume, itens_gerados)
    diversidade = calcular_diversidade(populacao)
    diversidade_por_geracao.append(diversidade)

# Gráfico da Diversidade da População
plt.figure(figsize=(10, 5))
plt.plot(diversidade_por_geracao, label="Diversidade Genética", color="purple")
plt.title("Diversidade da População ao Longo das Gerações")
plt.xlabel("Gerações")
plt.ylabel("Diversidade (variação média por gene)")
plt.legend()
plt.grid(True)
plt.show()

fitness_values = [fitness(ind, peso_maximo, capacidade_volume, itens_gerados) for ind in populacao]

# Plotando o histograma
plt.figure(figsize=(10, 6))
sns.histplot(fitness_values, bins=20, kde=True, color="coral")
plt.title("Distribuição de Fitness na População Final")
plt.xlabel("Fitness")
plt.ylabel("Frequência")
plt.grid(True)
plt.show()

# Calculando o peso e a necessidade total para cada indivíduo
pesos = [sum(itens_gerados[i]["peso"] for i, gene in enumerate(ind) if gene == 1) for ind in populacao]
valores = [sum(itens_gerados[i]["necessidade"] for i, gene in enumerate(ind) if gene == 1) for ind in populacao]

# Criando o gráfico de dispersão com cores diferentes para os pontos
plt.figure(figsize=(12, 8))

# Usando uma paleta de cores para variar os pontos de acordo com o valor da necessidade
scatter = plt.scatter(pesos, valores, c=valores, cmap="viridis", alpha=0.7)

# Adicionando título e rótulos
plt.title("Gráfico de Pareto: Peso vs Necessidade", fontsize=16)
plt.xlabel("Peso Total", fontsize=14)
plt.ylabel("Necessidade Total", fontsize=14)

# Adicionando barra de cores para indicar os valores da necessidade
plt.colorbar(scatter, label='Necessidade')

# Adicionando uma grade para facilitar a leitura
plt.grid(True, linestyle="--", alpha=0.7)

# Exibindo o gráfico
plt.show()
