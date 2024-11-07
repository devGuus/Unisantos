""" Preparar uma mochila para participar de um acampamento 
O objetivo é preencher uma mochila com diferentes objetos e pesos
buscando o maior valor possível sem ultrapassar o peso máximo"""

# Importando as fuções 
from FuncoesGenetica import *
import random

# Passando pesos e valores para geração aleatória
numero_itens = 10
min_peso, max_peso = 1, 100 # intervalo para pesos
min_valor, max_valor = 10, 400 # valor minimo e o maximo da mochila
peso_maximo = 100
numero_cromossomos = 150
geracoes = 80

# Gera uma lista de itens com [peso, valor]
itens = [[random.randint(min_peso, max_peso), random.randint(min_valor, max_valor)] for i in range(numero_itens)]

