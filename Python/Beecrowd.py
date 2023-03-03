# Como normalmente em qualquer aprendizagem de linguagem
# Começaremos com o Hello World!
# Exercicio N° 1000 beecrowd link: https://www.beecrowd.com.br/judge/pt/problems/view/1000

print("Hello World!")

# Exercicio N° 1002 Área do Círculo

raio = float(input())
n = 3.14159
area = n * (raio**2)
print("A=%.4f" %area)

#Exercicio  N° 1004 Produto Simples

valor1 = int(input())
valor2 = int(input())
prod = valor1 * valor2
print("PROD = %d" %prod)

# Exercicio N°1017 Gasto de combustível

tempoGasto = int(input())
vel = int(input())
cont = (tempoGasto * vel) / 12 # O carro faz 12Km/L
print("%.3f" %cont) # Somente 3 números após a virgula
