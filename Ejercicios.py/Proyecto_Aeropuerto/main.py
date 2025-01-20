import os
import pandas as pd
from entities.aeropuerto import Aeropuerto
from entities.lector import LectorCSV, LectorJSON, LectorTXT
from entities.lector import Lector

def preprocess_data(df_list):
    df_ = pd.concat(df_list)
    df_['fecha_llegada'] = df_['fecha_llegada'].apply(lambda x: x.replace('T',' '))
    df_['fecha_llegada'] = pd.to_datetime(df_['fecha_llegada'])
    return df_


if __name__ == '__main__':
    path_1 = os.path.abspath('./data/vuelos_1.txt')
    path_2 = os.path.abspath('./data/vuelos_2.csv')
    path_3 = os.path.abspath('./data/vuelos_3.json')

    lectortxt = LectorTXT(path_1)
    lectorcsv = LectorCSV(path_2) 
    lectorjson = LectorJSON(path_3)
    
    dtxt = lectortxt.lee_archivo()
    dftxt = lectortxt.convierte_dict_a_csv(dtxt)
    
    dfcsv = lectorcsv.lee_archivo()
    
    djson = lectorjson.lee_archivo()
    dfjson = lectorjson.convierte_dict_a_csv(djson)

    df = preprocess_data([dftxt, dfcsv, dfjson])
    
    aeropuerto = Aeropuerto(vuelos =df, slots = 3, t_embarque_nat =60, t_embarque_internat =100)
    aeropuerto.asigna_slots()


