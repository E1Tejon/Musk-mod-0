import os
import pandas as pd
import json

class Lector:
    def __init__(self, path: str):
        self.path = path

    def _comprueba_extension(self, extension):
        file_extension = os.path.splitext(self.path)[1]
        if file_extension != extension:
            raise Exception("El archivo no tiene la extensión correcta.")
        else:
            return True

    def lee_archivo(self):
        '''Lee archivos'''

    @staticmethod
    def convierte_dict_a_csv(list_dict: list[dict])->pd.DataFrame:
        df = pd.DataFrame.from_dict(list_dict)
        return df


class LectorCSV(Lector):

    def lee_archivo(self)->pd.DataFrame:
        df = None
        if super()._comprueba_extension('.csv'):
            df = pd.read_csv(self.path)
        return df 


class LectorJSON(Lector):

    def lee_archivo(self)->list[dict]:
        list_vuelos = []
        if super()._comprueba_extension(".json"):
            with open(self.path, 'r', encoding = "utf-8") as file:
                list_vuelos = json.load(file)
        return list_vuelos


class LectorTXT(Lector):

    def lee_archivo(self)->list[dict]:
        data = []
        if super()._comprueba_extension(".txt"):
            with open(self.path, 'r', encoding = "utf-8") as file:
                cabecera = file.readline().strip().split(", ")
                for linea in file:
                    valores = linea.strip().split(", ")
                    registro ={cabecera[i]: valores[i] for i in range(len(cabecera))}
                    data.append(registro)
        return data