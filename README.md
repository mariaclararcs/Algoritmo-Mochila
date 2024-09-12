# ALGORITMO MOCHILA
Este é um programa em Python que resolve uma variação simples do problema da mochila, onde temos um conjunto de clientes a serem atendidos, cada um com seu tempo de atendimento e prioridade, e o objetivo é maximizar a prioridade total das pessoas que podem ser atendidas no período máximo de tempo determinado.

## Descrição
O problema da mochila consiste em escolher clientes de um conjunto, de modo que a soma dos seus tempos de atendimento não ultrapasse a capacidade máxima da "mochila", ou seja, que o total do tempo de atendimento aos clientes não ultrapasse a capacidade determinada, e ao mesmo tempo, a soma das prioridades dos clientes selecionados seja maximizada.

Este programa gera tempo e prioridades aleatoriamente para um conjunto de clientes, cria uma solução inicial aleatória e avalia a qualidade dessa solução.

## Funcionalidades
- Gerar Problema: Cria um conjunto de pessoas com tempo e prioridades aleatórios.
- Solução Inicial: Gera uma solução inicial aleatória, preenchendo a mochila até sua capacidade máxima.
- Avaliação da Solução: Calcula a qualidade da solução, levando em conta as prioridades dos clientes.

**O programa contém as seguintes funções:**
- Gerar_Problema(n, me1, ma1, me2, ma2): Gera tempo e prioridades aleatórios para n pessoas.
- Solucao_Inicial(n, c_max, pe): Cria uma solução inicial aleatória, preenchendo a mochila até o limite de capacidade.
- Avalia(n, s, pe, pr): Avalia a solução gerada com base nas prioridades dos clientes incluídos na mochila.

## Exemplos de uso

**Definir parâmetros iniciais**  
N = 10 *(Número de clientes)*  
CAPACIDADE = 100 *(Capacidade máxima da mochila)*  
MIN_TP = 10 *(Tempo mínimo dos clientes)*  
MAX_TP = 50 *(Tempo máximo dos clientes)*  
MIN_PRI = 1 *(Prioridade mínima dos clientes)*  
MAX_PRI = 5 *(Prioridade máxima dos clientes)*  

**Gerar os tempo e prioridades aleatórios dos clientes**  
tempo, prior = Gerar_Problema(N, MIN_TP, MAX_TP, MIN_PRI, MAX_PRI)

**Criar a solução inicial**  
si = Solucao_Inicial(N, CAPACIDADE, tempo)

**Avaliar a solução inicial**  
vi = Avalia(N, si, tempo, prior)  

print("Tempos: ", tempo)  
print("Prioridades: ", prior)  
print("Solução Inicial: ", si)  
print("Avaliação da Solução: ", vi)  

**Exemplo de Saída:**  
Tempos:  [20 35 18 40 15 27 48 13 24 12]  
Prioridades:  [5 3 1 4 2 5 1 3 2 5]  
Solução Inicial: [0 1 0 0 1 1 0 1 0 1]  
Avaliação da Solução: 19  

## Como Executar:
Certifique-se de ter o Python instalado.
Clone este repositório ou copie o código para seu ambiente local.
Execute o programa em um terminal ou IDE Python com o comando:
```
python interface.py
```

## Requisitos:
- Python 3.x  
- Bibliotecas numpy e random, que já estão incluídas no Python padrão.

Você pode instalar o numpy com o seguinte comando, se necessário:
```
pip install numpy
```
