'''
Exibe dataset com dados do PISA
Compara dados do Brasil com os dos EUA e Suécia
dataset hospedado no Kaggle.
'''

import pandas as pd
import kagglehub

path = kagglehub.dataset_download("zazueta/pisa-scores-2015")
data = pd.read_csv(path+'/Pisa mean perfromance scores 2013 - 2015 Data.csv')

country_data = data.loc[(data['Country Code'] == 'BRA') |
                        (data['Country Code'] == 'USA') |
                        (data['Country Code'] == 'SWE')]

country_data
