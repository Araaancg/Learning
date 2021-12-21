# Datos abiertos de la c. Madrid, incidencia covid
import requests as req
import json
from obj_std import *

url = "https://datos.comunidad.madrid/catalogo/dataset/b3d55e40-8263-4c0b-827d-2bb23b5e7bab/resource/907a2df0-2334-4ca7-aed6-0fa199c893ad/download/covid19_tia_zonas_basicas_salud_s.json"
res = req.get(url).json()

with open("./covid.json",mode="w",encoding="utf8") as file:
    json.dump(res,file,indent=4,ensure_ascii=False)

def get_data(json_file):
    with open(json_file,encoding="utf8") as file:
        return json.load(file)

data = get_data("./covid.json")
last_date = data["data"][0]["fecha_informe"].split(" ")[0].replace("/","-")
# print(last_date)


# Función que convierte el data en un DICCIONARIO (keys: fechas, values: lista de info de cada municipio(dic))
def data_by_date(dataset):
    result = {}
    for zone in dataset["data"]:
        idate = zone["fecha_informe"].split(" ")[0]
        if result.get(idate):
            result[idate].append(zone)
        else:
            result[idate] = [zone]
    return result

data_by_date = data_by_date(data)



# CASOS CONFIRMADOS TOTALES
casos_totales = sum([zone["casos_confirmados_totales"] for zone in data_by_date["2021/12/07"]])

# CREAMOS UN OBJETO CCT (casos confirmados totales)
x = [num for num in range(0, len(data_by_date))] # Representa las semanas (de la primera a la 80)
y = [] 
for zones_by_date in data_by_date.values(): #valores de y
      y.append(sum(z["casos_confirmados_totales"] for z in zones_by_date))
y.reverse() 

analyze_cct = Std(x,y)
predicted_y = analyze_cct.lineals

# Predecir los casos en un día concreto
day_to_predict = analyze_cct.specific_date("2021-12-31",last_date)



# SAN SILVESTRE: Incidencia acumulada de el 2021/12/14 menor que el 2020/12/15
y_2020 = tuple([zone["tasa_incidencia_acumulada_ultimos_14dias"] for zone in data_by_date["2020/12/15"]])
y_2021 = tuple([zone["tasa_incidencia_acumulada_ultimos_14dias"] for zone in data_by_date["2021/12/14"]])
x = tuple(num for num in range(0, len(y_2020)))

# print(len(y_2020) == len(y_2021))

tia_year_2020 = Std(x,y_2020)
tia_year_2021 = Std(x,y_2021)

# print(f"MEDIA 2020: {tia_year_2020.y_avg}")
# print(f"MEDIA 2021: {tia_year_2021.y_avg}")


def ec_student(sample_1,sample_2):
        # NUMERADOR
        nu = sample_1.y_avg - sample_2.y_avg
        #DENOMINADOR
        raiz_first_piece = ((sample_1.n - 1) * sample_1.y_cuasivar + (sample_2.n - 1) * sample_2.y_cuasivar) / (sample_1.n + sample_2.n - 2)
        raiz_end_piece = ((1 / sample_1.n) + (1 / sample_2.n))
        de = (raiz_first_piece * raiz_end_piece) ** 0.5
        return nu / de

print(f"ec_student: {ec_student(tia_year_2021,tia_year_2020)}")

# print(f"CUASI 2021: {tia_year_2021.y_cuasivar}")
# print(f"CUASI 2020: {tia_year_2020.y_cuasivar}")
