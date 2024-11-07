# Preparando uma mochila para um acampamento
Este repositório implementa um algoritmo genético para resolver o problema da mochila, onde o objetivo é maximizar o valor dos itens escolhidos sem exceder um peso máximo.

##### Sequência do Algoritmo Genético
###### Inicialização: Cria-se uma população inicial de soluções candidatas.
###### Avaliação (Fitness): Cada indivíduo é avaliado com a função fitness.
###### Seleção de Pais: Indivíduos com melhor fitness são selecionados para reprodução.
###### Reprodução e Mutação: A partir dos pais, novos indivíduos são gerados com a possibilidade de mutação.
###### Nova Geração: O processo se repete com as novas gerações, visando a otimização da solução.
### Bibliotecas
O código usa apenas funções da biblioteca padrão do Python, como getrandbits, randint, random e choice, para geração de valores aleatórios e seleção.
![image](https://github.com/user-attachments/assets/ad26d8ea-bebc-4330-9c9e-5e4104f58108)

## Funções
### 1. individual(n_de_itens)
Cria um único indivíduo (ou cromossomo) representado como uma lista de bits (0s e 1s). Cada bit representa a presença (1) ou ausência (0) de um item na mochila. A função recebe o número de itens (n_de_itens) e gera uma lista de bits de comprimento igual a esse número.
![image](https://github.com/user-attachments/assets/228befae-0fe8-423c-9554-d337b91183c6)

### 2. population(n_de_individuos, n_de_itens)
Gera a população inicial do algoritmo genético, que é uma lista de indivíduos. Cada indivíduo é criado chamando a função individual(n_de_itens). A população inicial contém n_de_individuos indivíduos.
![image](https://github.com/user-attachments/assets/c7721e19-b29f-443d-9c2e-c9bdf8fa9da5)

### 3. fitness(individuo, peso_maximo, pesos_e_valores)
Avalia o fitness (aptidão) de um indivíduo:
Calcula o peso_total e o valor_total do indivíduo somando os pesos e valores dos itens incluídos (bits 1).
Se o peso_total exceder peso_maximo, retorna -1, indicando uma solução inválida.
Caso contrário, retorna o valor_total, que representa a qualidade do indivíduo. Quanto maior o valor, melhor a solução.
![image](https://github.com/user-attachments/assets/1bc94301-7602-4894-bf83-88fee1b9d289)


### 4. media_fitness(populacao, peso_maximo, pesos_e_valores)
Calcula a média de fitness da população, considerando apenas os indivíduos válidos (aqueles que não excedem o peso máximo). Retorna a média de fitness, útil para monitorar o desempenho médio da população ao longo das gerações.
![image](https://github.com/user-attachments/assets/f5be77a1-8048-4bf0-89e9-be77fc508c72)

### 5. selecao_roleta(pais)
Implementa a seleção por roleta:
Utiliza uma "roleta" baseada no fitness dos indivíduos, onde indivíduos com maior fitness têm maior chance de serem selecionados.
sortear é uma função auxiliar para realizar a seleção com a roleta, retornando o índice de um pai ou mãe.
Retorna um par de indivíduos (pai e mãe) para reprodução.
![image](https://github.com/user-attachments/assets/351625dd-661a-422a-94b5-cf898fed7259)

### 6. evolve(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos, mutate=0.05)
##### Realiza a evolução da população:
Seleciona os pais validos, filtrando e ordenando de acordo com seu fitness.

A reprodução gera novos indivíduos (filhos) ao combinar metade dos bits do pai e metade da mãe.

A mutação faz que o filho tenha uma pequena chance (mutate) de sofrer mutação, onde um bit aleatório é invertido (de 1 para 0 ou vice-versa), adicionando diversidade genética.
![image](https://github.com/user-attachments/assets/2e9bfcef-1089-4fe0-ac6e-453780419bd8)

### Parâmetros de Entrada
###### pesos_e_valores: Lista onde cada item é representado por [peso, valor]. No exemplo, são 10 itens com diferentes pesos e valores.
###### peso_maximo: Limite de peso que a mochila pode carregar (100).
###### n_de_cromossomos: Número de indivíduos em cada geração (150).
###### geracoes: Número de gerações que o algoritmo irá evoluir (80).
###### n_de_itens: Calculado com len(pesos_e_valores), representa o número total de itens disponíveis.
![image](https://github.com/user-attachments/assets/23cc7865-d11a-4aa8-8d2d-6f0ba79b369d)


## Executando o Algoritmo
### Criação da população e Evolução das Gerações
Inicializa-se a população com n_de_cromossomos indivíduos, onde cada indivíduo contém n_de_itens bits representando os itens escolhidos. 
Em seguida, o historico_de_fitness é inicializado com a média de fitness da população inicial.
##### Para cada geração:
###### A função evolve evolui a população, criando uma nova geração de indivíduos.
###### Calcula-se a média de fitness da nova geração e adiciona-se ao historico_de_fitness.
![image](https://github.com/user-attachments/assets/b123afaf-555e-466d-b933-7ebda17892ec)

### Resultados pelo Terminal
##### Ao final da execução, é mostrado no terminal alguns resultados:
###### Mostra-se o valor médio da mochila para cada geração, permitindo ver a melhoria ao longo das gerações.
###### Exibe-se o peso máximo e os itens disponíveis, com seus pesos e valores.
###### Exibe-se alguns exemplos de boas soluções na população final.
![image](https://github.com/user-attachments/assets/39aa3b16-6fb5-4574-b136-e4827cd3810a)

### Gráfico da Evolução do Fitness
![image](https://github.com/user-attachments/assets/dc7ff453-d401-4433-a6e1-520bf29afb81)

### Como Usar
Clone o repositório, configure os parâmetros desejados (como peso, peso maximo e número de cromossomos) e execute o script principal para observar a evolução das soluções geradas pelo algoritmo genético.
