#exercicio 1118 Beecrowd
cont = 0
while cont != 2:
  
  nota1 = float(input()) # recebendo as notas
  while nota1 < 0 or nota1 > 10: # verifica a nota 1
    print("nota invalida") # avisa valor invalido
    nota1 = float(input()) # recebe um novo valor

  nota2 = float(input())
  while nota2 < 0 or nota2 > 10: # verifica nota 2
    print("nota invalida") 
    nota2 = float(input())
    
  media = (nota1 + nota2) / 2 # calcula a media
  print("media =", media)
  
  opcao = 0
  while opcao != 1 and opcao != 2:
    opcao = int(input("novo calculo (1-sim 2-nao)\n"))
  
  if opcao == 2:
    break  
