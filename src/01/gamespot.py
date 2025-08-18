'''
usa pandas para exibir dataset de jogos do site gamespot.
dataset está hospedado no Kaggle.
'''

import pandas as pd
import kagglehub

path = kagglehub.dataset_download("dthectieve/gamespot-review")
data = pd.read_csv(path+'/dataset.csv')

#data #imprime os dados de forma bruta no notebook
data.describe() #mostra informações estatísticas básicas
