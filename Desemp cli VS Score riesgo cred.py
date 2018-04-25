# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:35:43 2018

@author: DAB97664
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import os
os.chdir(os.path.dirname('\\\srfspw001i005\\Riesgos_Personas\\Analisis_D4_D5\\TABLES\\'))

## calcula Porcentaje Buenos
def calc_porc_bueno(archivo):
    return (len(archivo[archivo['FLAG_Bueno'] == 1]) / len(archivo))*100

############################    
######## PARAMETROS ########
############################
archivo = pd.read_csv('TODO_SCORE_NOSIS_400.csv')
corte_score_ini = 0
corte_score_fin = 400
titulo_grafico = 'Tasa de clientes Buenos en SF de todos los clientes calificados por NOSIS con Score <= 400'

###################################################################

## Calculo % de Buenos por corte Score Nosis
for i in range(corte_score_ini , corte_score_fin + 1 ):
    porc_bueno = calc_porc_bueno(archivo[archivo['SCORE_NOSIS'] >= i])
    if(i == corte_score_ini):
        salida = pd.DataFrame( [[i,porc_bueno]], columns= ['SCORE_NOSIS', 'BUENOS'])
    else:
        a =pd.DataFrame( [[i,porc_bueno]], columns= ['SCORE_NOSIS', 'BUENOS']) 
        salida = salida.append(a)

## Calculo Max Tasa de Buenos.
Max_tasa_Buenos = salida['BUENOS'].max()  ## Max tasa de Buenos
b = salida[salida['BUENOS'] == salida['BUENOS'].max()]
Min_Score_Nosis_Max_tasaB = b['SCORE_NOSIS'].min()

## Gráfico
plt.scatter(salida['SCORE_NOSIS'], salida['BUENOS'], linewidths= 0.0001 )
plt.xlabel("SCORE_NOSIS")
plt.ylabel("% BUENOS")
plt.title(titulo_grafico)
plt.legend(loc=2)
plt.show()



