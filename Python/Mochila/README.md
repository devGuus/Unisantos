# Preparando uma mochila para um acampamento
Este repositório implementa um algoritmo genético para resolver o problema da mochila, onde o objetivo é maximizar o valor dos itens escolhidos sem exceder um peso máximo.

### Bibliotecas
O código usa apenas funções da biblioteca padrão do Python, como getrandbits, randint, random e choice, para geração de valores aleatórios e seleção.
![image](https://github.com/user-attachments/assets/ad26d8ea-bebc-4330-9c9e-5e4104f58108){: width="50%"}

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
![image](https://github.com/user-attachments/assets/134a4321-7b2c-4273-a979-9ea1ed1a3351)

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

##### Fluxo do Algoritmo Genético
###### Inicialização: Cria-se uma população inicial de soluções candidatas.
###### Avaliação (Fitness): Cada indivíduo é avaliado com a função fitness.
###### Seleção de Pais: Indivíduos com melhor fitness são selecionados para reprodução.
###### Reprodução e Mutação: A partir dos pais, novos indivíduos são gerados com a possibilidade de mutação.
###### Nova Geração: O processo se repete com as novas gerações, visando a otimização da solução.
####

Como Usar
Clone o repositório, configure os parâmetros desejados (como peso_maximo e n_de_cromossomos) e execute o script principal para observar a evolução das soluções geradas pelo algoritmo genético.
