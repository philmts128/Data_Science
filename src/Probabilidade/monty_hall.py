'''
Simulação do problema de Monty Hall
Usando a Lei ds Grandes Números, se prova que vle mais a pena trocar de escolha
'''

import numpy as np


#--------------------------------------
MAX_ITERATIONS = 100000


#abaixo é a simulação da condição da pessoa escolher uma porta e NÃO mudar
#probabilidade teórica de ganhar é 1/3
#--------------------------------------
def simulation_no_change(tries = 1000):
    results = {} #registra frequência de sucessos e fracassos: X = 0 para fracasso e X = 1 para sucesso

    for i in range(0, tries):
        prize  = np.random.randint(1, 4) #número da porta a ser escohida: {1, 2, 3}
        choice = np.random.randint(1, 4) #número que o participante escolhe
        if (prize == choice):
            results[1] = results.get(1, 0) + 1
        else:
            results[0] = results.get(0, 0) + 1

    return results
#--------------------------------------

#--------------------------------------
def no_change_test():
    print('-- O Participante Nunca Muda de Porta --')
    res = simulation_no_change(MAX_ITERATIONS)
    print('Sucessos: {}'.format(res[1]))
    print('Fracassos: {}'.format(res[0]))
    prob_suc = res[1] / (res[0] + res[1])
    print('Probabilidade de sucesso: {:.3f}'.format(prob_suc))
    print('Probabilidade de fracasso: {:.3f}'.format(1-prob_suc))
#--------------------------------------

#abaixo é a simulação da condição da pessoa escolher uma porta e mudar
#probabilidade teórica de ganhar é 2/3

#--------------------------------------
def get_empty_door(selected_door, prize_door):
    if (selected_door == prize_door):
        x = np.random.randint(1, 4)
        while (x == prize_door):
            x = np.random.randint(1, 4)
        return x
    else:
        return (6 - (selected_door + prize_door))
#--------------------------------------

#--------------------------------------
def select_new_door(empty_door):
    x = np.random.randint(1, 4) #de 1 à 3
    if (x == empty_door):
        return select_new_door(empty_door)
    else:
        return x
#--------------------------------------

#--------------------------------------
def simulation_change(tries = 1000):
    results = {} #registra frequência de sucessos e fracassos: X = 0 para fracasso e X = 1 para sucesso

    for i in range(0, tries):
        prize  = np.random.randint(1, 4) #número da porta a ser escohida: {1, 2, 3}
        choice = np.random.randint(1, 4) #número que o participante escolhe

        #se o candidato escolhe errado na primeira vez e muda a porta, ele sempre ganha
        #se o candidato acerta na primeira vez e muda, ele sempre perde
        #logo, pelas regrs da adição e multiplicação da probabilidade, se a probabilidade de ganhar
        #será a mesma de ele perder caso não tivesse mudado de porta
        if (prize != choice):
            results[1] = results.get(1, 0) + 1
        else:
            results[0] = results.get(0, 0) + 1

    return results
#--------------------------------------

#--------------------------------------
def change_test():
    print('-- O Participante Sempre Muda de Porta --')
    res = simulation_change(MAX_ITERATIONS)
    print('Sucessos: {}'.format(res[1]))
    print('Fracassos: {}'.format(res[0]))
    prob_suc = res[1] / (res[0] + res[1])
    print('Probabilidade de sucesso: {:.3f}'.format(prob_suc))
    print('Probabilidade de fracasso: {:.3f}'.format(1-prob_suc))
#--------------------------------------


#--------------------------------------
def main():
    no_change_test()
    print()
    change_test()

if __name__ == "__main__":
    main()
#--------------------------------------
