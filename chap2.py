# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:30:47 2017

@author: USER_
"""

# -----------------------------------------------------
# Chapter 2: ToolBoxes for Data Scientists
# -----------------------------------------------------

import pandas as pd
import numpy as np

# The Dataframe with DataStructure

data = {
        'year': [
            2010, 2011, 2012, 
            2013, 2014, 2015,
            2016, 2017, 2018
        ],
        'team': [
            'Barcelona', 'Chelsea', 'Bayern',
            'Real Madrid', 'Barcelona', 'Real Madrid',
            'Real Madrid', 'PSG', 'Manchester City'
        ],
        'wins': [
            30, 28, 32, 
            29, 32, 26,
            21, 17, 19
        ],
        'draws': [
            6, 7, 4, 
            5, 4, 7,
            8, 10, 8
        ],
        'losses': [
            2, 3, 2,  
            4, 2, 5,
            9, 11, 11 
        ]
}

football = pd.DataFrame(data, columns = [
    'year', 'team', 'wins', 'draws', 'losses'        
])


#-- manipulacao de dados usando pandas --

#levar os dados do formato csv para um dataframe de python
edu = pd.read_csv('educ_figdp_1_Data.csv', na_values = ':',usecols = [
        "TIME","GEO","Value"])

#listar primeiros elementos do dataframe
print(edu.head(10))

#listar ultimos elementos do dataframe
print(edu.tail(10))

#dados estatisticos principais
print(edu.describe())

#selecionar dados
print(edu['TIME'].head(10))
print(edu['Value'].tail(10))
print(edu[10:14])
print(edu[10:14]['TIME'])
print(edu.ix[90:94, ['TIME','GEO']])

#filtragem de dados
print(edu[edu['Value']>6.5])
print(edu[edu['Value']>6.5].tail())
print(edu[edu['Value']>6.5].head())

#filtragem de valores NaN 
print(edu[edu['Value'].isnull()])
print(edu[edu['Value'].isnull()].count())
print(edu.max(axis = 0))
# axis = 0 ==> rows  |  axis = 1 ==> columns

#funcao maximo para python
print(max(edu['Value']))

#funcao maximo para pandas
print(edu['Value'].max())
print((edu['Value']/100).head())

#aplicacao de funcoes matematicas
s = edu['Value'].apply(np.sqrt)
t = edu['Value'].apply(np.log10)
print(s.head())
print(t.head())

#funcao lambda <funcao matematica definida pelo usuario>
s = edu['Value'].apply(lambda x: x**2)
print(s.head(10))

#criacao de uma nova medida apartir de uma funcao matematica
edu['ValueNorm'] = edu['Value'] / edu['Value'].max()
edu['ValueLog'] = edu['Value'].apply(np.log10)
edu['ValueUser'] = edu['Value'].apply(lambda x: x**2)
print(edu.head(10))

#funcao append como insertor de dados
edu = edu.append({'TIME': 2000, 'GEO': 'a', 'Value': 5.00}, ignore_index = True)
print(edu.tail())

#funcao drop como eliminador de dados
edu.drop(max(edu.index), axis = 0, inplace = True)
# elimina a fila com o maior indice e nao faz copia do valor original
print(edu.tail())

#eliminar missing values
eduDrop = edu.drop(edu['Value'].isnull(), axis = 0)
print(eduDrop.head())

#outra forma com uma funcao generica
eduDrop = edu.dropna(how = 'any', subset = ['Value'])
print(eduDrop)

#preencher valores nulos
eduFilled = edu.fillna(value = {'Value': edu['Value'].mean()})

#ordenacao de dados
edu.sort_values(by = 'Value', ascending = True, inplace = True)
print(edu.head())

#agrupamento de dados
grupo1 = edu[['GEO', 'Value']].groupby('GEO').mean()
print(grupo1)

#filtragem ao estilo select from
dados_filter = edu[edu['TIME']>2005]

#rearranjo <forma mais complexa de agrupamento> de dados
import pandas as pd
tbl = pd.pivot_table(dados_filter, values = 'Value', index = ['GEO'], columns = ['TIME'])
print(tbl)

amostra = tbl.ix[['France', 'Spain'], [2009,2010, 2011]]
print(amostra)

#eliminar filas de acordo com os indices
tbl = tbl.drop([
    'Euro area (13 countries)', 'Euro area (15 countries)', 'Euro area (17 countries)',
    'Euro area (18 countries)', 'European Union (25 countries)', 'European Union (27 countries)',
    'European Union (28 countries)'], axis = 0)

#editar indice de uma fila 
tbl = tbl.rename(index = {'Germany (until 1990 former territory of the FRG)' : 'Germany'})

#eliminar filas com dados NaN
tbl = tbl.dropna()

#ordenacao dos dados
tbl.rank(ascending = False, method = 'first')

#organizar dados pela soma dos valores de receita dos ultimos 6 anos
total_tbl = tbl.sum(axis = 1)

total_tbl.rank(ascending = False, method = 'dense').sort_values()

# method first ==> recebe uma posicao no ranking diferente
# method dense ==> recebe uma posicao = em caso de empate

# plotting

#obter o total de receita dos ultimos 6 anos em ordem descendente
totalSum = tbl.sum(axis = 1).sort_values(ascending = False)

#graficar os resultados
# kind => tipo de grafico || style => cor blue || alpha => intensidade, brilho
totalSum.plot(kind = 'bar', style = 'b', alpha = 0.5, title = 'Total Renenue')

#grafica por anos 2006 || 2011
my_colors = ['b', 'r', 'g', 'y', 'm', 'c']
# kind => tipo de grafico || stacked => nro de series
ax = tbl.plot(kind = 'barh', stacked = True, color = my_colors)
ax.legend(loc = 'center left', bbox_to_anchor = (2, 1))

