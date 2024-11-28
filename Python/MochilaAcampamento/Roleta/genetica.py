from random import getrandbits, randint, random, choice
import urllib.request

def carregar_itens(link):
    response = urllib.request.urlopen(link)
    data = response.read().decode("utf-8")
    itens = []
    for linha in data.strip().split("\n"):
        nome, peso, necessidade, volume, categoria = linha.split(",")
        itens.append({
            "nome": nome,
            "peso": int(peso),
            "necessidade": int(necessidade),
            "volume": int(volume),
            "categoria": categoria
        })
    return itens

categorias_obrigatorias = {"comida"}  # Categorias essenciais para viabilidade

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
    itens_selecionados = set()

    for indice, valor in enumerate(individuo):
        if valor == 1:  # Se o item foi selecionado
            item = itens[indice]
            categoria = item["categoria"]
            identificador = f"{categoria}-{indice}"

            # Penalizar duplicados
            if identificador in itens_selecionados:
                return -1
            itens_selecionados.add(identificador)

            # Soma peso, valor e volume
            peso_total += item["peso"]
            necessidade_total += item["necessidade"]
            volume_total += item["volume"]

            # Rastrear categorias selecionadas
            categorias_selecionadas.add(categoria)

    # Penalizar se exceder peso ou volume máximo
    if peso_total > peso_maximo or volume_total > capacidade_volume:
        return -1

    # Penalidades dinâmicas
    faltantes = categorias_obrigatorias - categorias_selecionadas
    if faltantes:
      penalidade = 100  # Penalidade significativa por categoria ausente
      necessidade_total -= penalidade * len(faltantes)

    return necessidade_total if necessidade_total > 0 else -1  # Garantir fitness não negativo

# Função de seleção por roleta viciada
def selecao_roleta(pais):
    def sortear(fitness_total, indice_a_ignorar=-1):
        roleta, acumulado, valor_sorteado = [], 0, random()
        if indice_a_ignorar != -1:
            fitness_total -= valores[0][indice_a_ignorar]
        for indice, i in enumerate(valores[0]):
            if indice == indice_a_ignorar:
                continue
            acumulado += i
            roleta.append(acumulado / fitness_total)
            if roleta[-1] >= valor_sorteado:
                return indice

    valores = list(zip(*pais))
    fitness_total = sum(valores[0])

    indice_pai = sortear(fitness_total)
    indice_mae = sortear(fitness_total, indice_pai)

    pai = valores[1][indice_pai]
    mae = valores[1][indice_mae]

    return pai, mae

# Função para evolução da população
def evolve(populacao, peso_maximo, capacidade_volume, itens, n_de_cromossomos, mutate=0.05):
    pais = [
        [fitness(x, peso_maximo, capacidade_volume, itens), x]
        for x in populacao
        if fitness(x, peso_maximo, capacidade_volume, itens) >= 0
    ]
    pais.sort(reverse=True)

    # Reprodução
    filhos = []
    while len(filhos) < n_de_cromossomos:
        homem, mulher = selecao_roleta(pais)
        meio = len(homem) // 2
        filho = homem[:meio] + mulher[meio:]
        filhos.append(filho)

    # Mutação
    for individuo in filhos:
        if mutate > random():
            pos_to_mutate = randint(0, len(individuo) - 1)
            individuo[pos_to_mutate] = 1 - individuo[pos_to_mutate]  # Troca entre 0 e 1

    return filhos