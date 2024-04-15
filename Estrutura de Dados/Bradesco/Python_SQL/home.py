import mysql.connector

mybd = mysql.connector.connect( # Conectando ao servidor local do BD
    host = 'localhost',
    user = "Xavier",
    password = "22102003",
    database = "bdfirst",
)

mycursor = mybd.cursor() # mycursor será o nosso cursor
# Função para inserir produto na tabela
def Create(nome_produto, valor): 
    command = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    mycursor.execute(command)
    mybd.commit()
# Função para printar tabela
def Read(): 
    command = 'SELECT * FROM vendas'
    mycursor.execute(command)
    result = mycursor.fetchall() # Leia o BD
    print(result)
# Função para atualizar algum valor
def Update(nome_produto, valor): # Escolhi mudar somente o valor na tabela
    command = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    mycursor.execute(command)
    mybd.commit()
# Função de deletar
def Delete(coluna, item): 
    command = f'DELETE FROM vendas WHERE {coluna} = "{item}"'
    mycursor.execute(command)
    mybd.commit()

escolha = 5  # inicialize escolha fora do loop para que ele possa ser verificado na condição inicial

while escolha != 0:  # repete até escolha ser = 0
    escolha = int(input("(1)-Inserir (2)-Ler (3)-Atualizar (4)-Deletar "))  # solicita a escolha ao usuário

    if escolha == 1: # Insere o item
        nome_produto = input('Digite o nome do produto: ')
        valor = int(input('Digite o valor do produto: '))
        Create(nome_produto, valor)
    elif escolha == 2: # Lê e imprime a tabela
        Read()
    elif escolha == 3: # Atualiza o valor da tabela
        nome_produto = input('Digite o nome do produto: ')
        valor = int(input('Digite o valor do produto: '))
        Update(nome_produto, valor) 
    elif escolha == 4: # Seleciona o modo de escolha para excluir 
        escolha_coluna = int(input('(1)-ID (2)-Nome do produto (3)-valor: '))
        if escolha_coluna == 1:
            id = int(input("Digite o ID: "))
            Delete("idVendas", id)
        elif escolha_coluna == 2:
            nome_produto = input('Digite o nome do produto a ser deletado: ')
            Delete("nome_produto", nome_produto)
        elif escolha_coluna == 3:
            valor = int(input('Digite o valor a ser deletado: '))
            Delete("valor", valor)
        else:
            print('Digitou um valor invalido! ENCERRANDO...')
    else:
        print('VALOR INVALIDO')

mycursor.close()
mybd.close()