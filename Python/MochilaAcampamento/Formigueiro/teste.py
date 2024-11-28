import random
import matplotlib.pyplot as plt

# Parâmetros do problema
n_itens = 20  # Número de itens
capacidade_mochila = 50  # Capacidade máxima da mochila
categorias = ["comida", "água", "ferramenta", "conforto"]
n_formigas = 30  # Número de formigas
n_iteracoes = 100  # Número de iterações
taxa_evaporacao = 0.01  # Diminui a evaporação para preservar mais o feromônio
alpha = 0.5  # Menor influência do feromônio
beta = 3  # Maior influência da heurística (valor/peso)

# Função para gerar itens aleatórios
def gerar_itens(n):
    return [
        {
            "id": i + 1,
            "valor": random.randint(1, 20),  # Valor entre 1 e 20
            "peso": random.randint(1, 10),  # Peso entre 1 e 10
            "categoria": random.choice(categorias),
        }
        for i in range(n)
    ]

# Inicializar os itens
itens = gerar_itens(n_itens)

# Inicialização do feromônio (todos os itens começam com o mesmo valor de feromônio)
feromonio = {item["id"]: 1.0 for item in itens}

# Função para calcular a heurística (valor/peso)
def heuristica(item):
    return item["valor"] / item["peso"]

# Função para escolher um item com base no feromônio e na heurística
def escolher_item(itens_disponiveis, feromonio, alpha, beta):
    probabilidades = []
    for item in itens_disponiveis:
        tau = feromonio[item["id"]] ** alpha
        eta = heuristica(item) ** beta
        probabilidades.append(tau * eta)
    
    soma_prob = sum(probabilidades)
    probabilidades = [p / soma_prob for p in probabilidades]
    
    return random.choices(itens_disponiveis, weights=probabilidades, k=1)[0]

# Função para construir uma solução para cada formiga
def construir_solucao(itens, feromonio):
    mochila = []
    peso_atual = 0
    itens_disponiveis = itens[:]
    
    while itens_disponiveis:
        item = escolher_item(itens_disponiveis, feromonio, alpha, beta)
        if peso_atual + item["peso"] <= capacidade_mochila:
            mochila.append(item)
            peso_atual += item["peso"]
        itens_disponiveis.remove(item)
        
    return mochila

# Função para atualizar o feromônio após cada iteração
def atualizar_feromonio(feromonio, melhores_solucoes):
    # Evaporação do feromônio
    for item_id in feromonio:
        feromonio[item_id] *= (1 - taxa_evaporacao)
    
    # Reforço do feromônio nos melhores itens
    for solucao in melhores_solucoes:
        for item in solucao:
            feromonio[item["id"]] += item["valor"]

# ACO principal
melhor_solucao_global = []
melhor_valor_global = 0
historico_valores = []  # Para armazenar o valor total a cada iteração
historico_pesos = []  # Para armazenar o peso total a cada iteração

# Loop de iterações
for iteracao in range(n_iteracoes):
    solucoes = []
    valores = []
    pesos = []
    
    # Cada formiga constrói sua solução
    for _ in range(n_formigas):
        solucao = construir_solucao(itens, feromonio)
        valor = sum(item["valor"] for item in solucao)
        peso = sum(item["peso"] for item in solucao)
        
        # Verifica se a solução não ultrapassou a capacidade da mochila
        if peso <= capacidade_mochila:
            solucoes.append(solucao)
            valores.append(valor)
            pesos.append(peso)
    
    # Se houver soluções válidas, encontramos a melhor da iteração
    if valores:
        melhor_valor_iteracao = max(valores)
        melhores_solucoes = [solucoes[i] for i in range(len(valores)) if valores[i] == melhor_valor_iteracao]
        
        # Atualiza a melhor solução global
        if melhor_valor_iteracao > melhor_valor_global:
            melhor_valor_global = melhor_valor_iteracao
            melhor_solucao_global = melhores_solucoes[0]
        
        # Atualiza o feromônio com base nas melhores soluções
        atualizar_feromonio(feromonio, melhores_solucoes)
    
    # Armazena o valor e peso da melhor solução para análise
    historico_valores.append(melhor_valor_global)
    historico_pesos.append(sum(item["peso"] for item in melhor_solucao_global))

    print(f"Iteração {iteracao + 1}: Melhor Valor = {melhor_valor_global}, Peso Total = {sum(item['peso'] for item in melhor_solucao_global)}")

# Gráfico de Pareto: Peso vs Necessidade (Valor)
plt.figure(figsize=(12, 8))
plt.scatter(historico_pesos, historico_valores, c=historico_valores, cmap="viridis", alpha=0.7)
plt.title("Gráfico de Pareto: Peso vs Necessidade", fontsize=16)
plt.xlabel("Peso Total", fontsize=14)
plt.ylabel("Necessidade Total (Valor)", fontsize=14)
plt.colorbar(label='Necessidade (Valor)')
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

# Gráfico de Evolução do Melhor Valor ao Longo das Iterações
plt.figure(figsize=(12, 8))
plt.plot(historico_valores, label="Melhor Valor Total")
plt.title("Evolução do Melhor Valor Total ao Longo das Iterações", fontsize=16)
plt.xlabel("Iterações", fontsize=14)
plt.ylabel("Valor Total", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.show()
