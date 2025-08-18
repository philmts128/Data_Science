'''
seleção simples de linha num arquivo csv
dataset hospedado no Kaggle.
'''

import pandas as pd
import kagglehub

path = kagglehub.dataset_download("dthectieve/gamespot-review")
data = pd.read_csv(path+'/dataset.csv')

data['score'] #imprime uma das colunas

#imprime uma coluna
data.iloc[52,:]
