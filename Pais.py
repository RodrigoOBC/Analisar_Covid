import json
import pandas as pd


class Pais:
    def __init__(self, json_pais):
        self.dic_informacoes_pais = json.loads(json_pais)['countrytimelinedata'][0]
        self.dic_serie_pais_data_valor = json.loads(json_pais)['timelineitems'][0]
        self.id = self.dic_informacoes_pais['info']["ourid"]
        self.titulo = self.dic_informacoes_pais['info']["title"]
        self.code = self.dic_informacoes_pais['info']["code"]

    def transformar_df(self):
        casos, morte, recuperados, data = [], [], [], []
        for datas in self.dic_serie_pais_data_valor:
            if datas != 'stat':
                data.append(datas)
                casos.append(self.dic_serie_pais_data_valor[datas]['total_cases'])
                morte.append(self.dic_serie_pais_data_valor[datas]['total_deaths'])
                recuperados.append(self.dic_serie_pais_data_valor[datas]['total_recoveries'])
        df_pais_casos = pd.DataFrame(data={"Data": data, "Casos": casos, "Mortes": morte, "Recuperados": recuperados})
        return df_pais_casos
