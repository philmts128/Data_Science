'''
exibe os jogos avaliados na gamespot com melhor nota
obs: dataset hospedado no Kaggle.
'''

import pandas as pd
import kagglehub

path = kagglehub.dataset_download("dthectieve/gamespot-review")
data = pd.read_csv(path+'/dataset.csv')

#ordena pela nota
sorted_data = data.sort_values(by='score', ascending=False)

sorted_data.head(30) #limita 30 linhas

