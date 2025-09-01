'''
Simulação do problema de Monty Hall por meio de força-bruta (sem recorrer à análise e propriedades da probabilidade)
Mostra pela lei dos grande números que se você sempre mudar a porta no problema de Monty Hall,
a probabilidade de ganhar sempre será 2/3.

Depois disso plota um gráfico mostrando que os dados da simulação convergem para 2/3
'''

import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


#--------------------------------------
MAX_ITERATIONS = 2000


#abaixo é a simulação da condição da pessoa escolher uma porta e mudar
#probabilidade teórica de ganhar é 2/3

#--------------------------------------
def simulate():
    prize = np.random.randint(1, 4) #a porta onde está o prêmio
    choice = np.random.randint(1, 4) #primeir escolha do jogador
    doors = [1,2,3] #cada inteiro representa uma porta

    #o apresentador escolhe uma porta vazia e que não seja a porta que o participante escolheu
    empty = np.random.randint(1, 4)
    while (empty == prize or empty == choice):
        empty = np.random.randint(1, 4)
    doors.remove(empty) #o jogdor não escolhe essa porta vazia que o apresentador mostrou

    #o jogador sempre vai mudr de porta, então a porta que ele escolheu de primeira
    doors.remove(choice)

    return int(doors[0] == prize) # se ganhou, retorna 1, se perdeu, retorna 0
#--------------------------------------

#--------------------------------------
def test_simulation(iterations):
    data = {}
    for i in range(iterations):
        k = simulate()
        data[k] = data.get(k, 0) + 1

    p = data[1] / (data[0] + data[1])
    print('Probabilidade de ganhar: {:.3f}'.format(p))
    print('Probabilidade de perder: {:.3f}'.format(1-p))
#--------------------------------------

#--------------------------------------
def get_plot_data():
    data = {}
    for i in range(100, MAX_ITERATIONS + 100):
        prob = {}
        for j in range(i):
            k = simulate()
            prob[k] = prob.get(k, 0) + 1
        p = prob[1] / (prob[0] + prob[1])
        data[i] = p
    return data
#--------------------------------------

#--------------------------------------
def plot_graph(data):
    data = get_plot_data()
    sb.scatterplot(x = list(data.keys()), y = list(data.values()))
    plt.title('Lei dos Grandes Números')
    plt.show()
#--------------------------------------

#--------------------------------------
def main():
    test_simulation(MAX_ITERATIONS)
    plot_graph(get_plot_data())

if __name__ == "__main__":
    main()
#--------------------------------------
