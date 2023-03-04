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

# Exercicio 1021 Notas e Moesda

money = float(input())  # Recebe o valor a ser dividido

cem = cinquenta = vinte = dez = cinco = dois = um = 0
cents = cintecents = vintecents = dezcents = cincocents = cinquentacents = 0
# reais
money = float("%.2f" % money)
if int(money/100) >= 1:
    cem = int(money/100)
    money -= cem*100

money = float("%.2f" % money)
if int(money/50) >= 1:
    cinquenta = int(money/50)
    money -= cinquenta*50

money = float("%.2f" % money)
if int(money/20) >= 1:
    vinte = int(money/20)
    money -= vinte*20

money = float("%.2f" % money)
if int(money/10) >= 1:
    dez = int(money/10)
    money -= dez*10

money = float("%.2f" % money)
if int(money/5) >= 1:
    cinco = int(money/5)
    money -= cinco*5

money = float("%.2f" % money)
if int(money/2) >= 1:
    dois = int(money/2)
    money -= dois*2

#centavos

money = float("%.2f" % money)
if int(money/1) >= 1:
    um = int(money/1)
    money -= um*1

money = float("%.2f" % money)
if int(money/0.50) >= 1:
    cinquentacents = int(money/0.50)
    money -= cinquentacents*0.50

money = float("%.2f" % money)
if int(money/0.25) >= 1:
    vintecents = int(money/0.25)
    money -= vintecents*0.25

money = float("%.2f" % money)
if int(money/0.10) >= 1:
        dezcents = int(money/0.10)
        money -= dezcents*0.10

money = float("%.2f" % money)
if int(money / 0.05) >= 1:
    cincocents = int(money / 0.05)
    money -= cincocents*0.05

money = float("%.2f" % money)
if int(money / 0.01) >= 1:
    cents = int(money / 0.01)
    money -= cents*0.01

print("NOTAS:") # Imprime os valores
print("%d nota(s) de R$ 100.00" % cem)
print("%d nota(s) de R$ 50.00" % cinquenta)
print("%d nota(s) de R$ 20.00" % vinte)
print("%d nota(s) de R$ 10.00" % dez)
print("%d nota(s) de R$ 5.00" % cinco)
print("%d nota(s) de R$ 2.00" % dois)

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % um)
print("%d moeda(s) de R$ 0.50" % cinquentacents)
print("%d moeda(s) de R$ 0.25" % vintecents)
print("%d moeda(s) de R$ 0.10" % dezcents)
print("%d moeda(s) de R$ 0.05" % cincocents)
print("%d moeda(s) de R$ 0.01" % cents)

