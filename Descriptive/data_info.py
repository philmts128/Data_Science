'''
Script para achar informação básica de uma amostra:
média, mediana, variância e desvio padrão
Obs: instalar o matplotlib (pip install matplotlib)

Autor: Philippe Matias
'''

import re
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict


#------------------------------------------------
def input_data():
	datasets = []
	n = input('| entre com quantos datasets você deseja: ')
	for i in range(int(n)):
		a = input('| entre com a descrição e dados [ex: idades | 17 30 55]: ').split('|')
		name = a[0]
		data = data_list_from_str(a[1])
		datasets.append((data, name))
	return datasets
#------------------------------------------------

#------------------------------------------------
def output_data(datasets):
	for ds in datasets:
		_mean = mean(ds[0])
		_median = median(ds[0])
		_var = variance(ds[0])
		_sd = deviation(ds[0])
		name = ds[1]
		print('*------------------------------*')
		print('| nome: {}'.format(name))
		print('| média: {}'.format(_mean))
		print('| mediana: {}'.format(_median))
		print('| variância: {}'.format(_var))
		print('| desvio padrão: {}'.format(_sd))
		print('*------------------------------*')
	dot_plot(datasets)
#------------------------------------------------

#------------------------------------------------
def dot_plot(data_series):
	fig, ax = plt.subplots(figsize=(6, 3))
	altura_ponto = 0.15  # Espaçamento vertical entre bolinhas
	cores = plt.cm.get_cmap('tab10', len(data_series))  # Paleta com cores distintas

	for i, (dados, rotulo) in enumerate(data_series):
		contagem = defaultdict(int)
		cor = cores(i)  # Cor distinta para o grupo

		for x in dados:
			y = i + contagem[x] * altura_ponto
			ax.scatter(x, y, color=cor, label=rotulo if contagem[x] == 0 else "", alpha=0.8, edgecolors='black', linewidth=0.5)
			contagem[x] += 1

	ax.set_yticks(range(len(data_series)))
	ax.set_yticklabels([rotulo for _, rotulo in data_series])
	ax.set_xlabel("Dado")
	ax.set_title("Dot Plot")
	ax.legend()
	ax.grid(True, axis='x', linestyle='--', alpha=0.5)
	plt.tight_layout()
	plt.show()
#------------------------------------------------

#------------------------------------------------
def data_list_from_str(str_data):
	values_str = re.findall(r'-?\d+(?:\.\d+)?', str_data)
	return [float(num) for num in values_str]
#------------------------------------------------

#------------------------------------------------
def minimum(data):
	m = data[0]
	for i in range(1, len(data)):
		m = data[i] if (data[i] < m) else m
	return m
#------------------------------------------------

#------------------------------------------------
def mean(data):
	sum = 0.0
	for i in data:
		sum += i
	return sum / len(data)
#------------------------------------------------

#------------------------------------------------
def median(data):
	data.sort()
	size = len(data)
	half = math.floor(size/2)
	if (size % 2 != 0):
		return (data[half])
	else:
		a = data[half-1]
		b = data[half]
		return (a + b)/2.0
#------------------------------------------------

#------------------------------------------------
def variance(data):
	x = mean(data)
	v = 0.0
	for i in data:
		v += (i - x)**2
	return v/(len(data)-1)
#------------------------------------------------

#------------------------------------------------
def deviation(data):
	return math.sqrt(variance(data))
#------------------------------------------------


#------------------------------------------------
def main():
	output_data(input_data())

if __name__ == '__main__':
	main()
#------------------------------------------------