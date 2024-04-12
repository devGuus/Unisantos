def verificar_veiculo(veiculo, passageiros):
    maximo_carro = 4
    maximo_moto = 1

    if veiculo == 1:
        if passageiros <= maximo_carro:
            return print("Verificado")
        else:
            return print('Quantidade de passageiros não permitido')    

iniciar_viagem = int(input("Deseja iniciar uma viagem?"))

if(iniciar_viagem == 1):
    print('iniciando rota')
    veiculo = input("Qual veiculo deseja utilizar? 1 Padrão - 2 Premium - 3 Moto - 4 Delivery")
    passageiros = int(input('Quantos passageiros?'))
    print(verificar_veiculo(veiculo, passageiros))
elif(iniciar_viagem == 0):
    print('Encerrando corrida')
else:
    print('Resposta incorreta')