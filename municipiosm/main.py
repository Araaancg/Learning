import requests as req
import csv
import json

'''
Ejercicio municipios Madrid
Al principio trabajamos con csv y al final convertiremos el archivo en un json

Obtener:
- El municipio por INE
- El municipio más grande
- Superficie total
- Densidad total
- Población total de Madrid
- Población media de los municipios
- Comprobar la ley de benford con la superficie
- Convertir el csv en un json
'''

# Primero importamos la data de la pag web oficial de la c. de Madrid (en csv)

url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/ee750429-1e05-411a-b026-a57ea452a34a/download/municipio_comunidad_madrid.csv"
res = req.get(url).content
# La info esta codificada asi que la tenemos que decodificar. Las tildes y ñ's quedan como ?
res = res.decode("utf-8",errors="replace")
# El replace los reemplaza con la "?", el ignore los eliminaría pero perdemos info

# with open("data_municipios.csv", mode="w", encoding="utf8") as file:
#     file.write(res)

# Ya tenemos el archivo escrito

# EJERCICIO 1: Obtener el municipio por código INE
def get_by_ine(dataset, ine_code):
    for mun in dataset[1:]: # El [1:] para que no coja la primera línea que son los headings
        if mun[2] == ine_code:
            return mun

# EJERCICIO 2: Obtener el municipio más grande
def get_biggest_mun(dataset):
    biggest_area = 0
    biggest_mun = None
    for mun in dataset[1:]:
        if float(mun[-2]) > biggest_area:
            biggest_area = float(mun[-2])
            biggest_mun = mun
    return biggest_mun

# EJERCICIO 3: Obtener la superficie total
def get_sup_total(dataset):
    sup_total = 0
    for mun in dataset[1:]:
        sup_total += float(mun[-2])
    return sup_total

# EJERCICIO 4: Obtener la densidad total
def get_total_density(dataset):
    total_density = 0
    for mun in dataset[1:]:
        total_density += float(mun[-1])
    return total_density

# EJERCICIO 5: Obtener la población total (densidad*superficie)
def get_total_population(dataset):
    total_population = 0
    for mun in dataset[1:]:
        local_population = float(mun[-2])*float(mun[-1])
        total_population += local_population
    return total_population

# EJERCICIO 6: Población de media entre todos los municipios
def get_average_population(dataset):
    total_population = 0
    for mun in dataset[1:]:
        local_population = float(mun[-2])*float(mun[-1])
        total_population += local_population
    average_population = total_population/len(dataset[1:])
    return average_population

# EJERCICIO 7: Comprobar la ley de benford
def benford(dataset):
    densities = [mun[-2] for mun in dataset[1:]]
    result = {}
    for num in range(1,10):
        result[str(num)] = []
    for num in result.keys():
        for density in densities:
            if density.startswith(num):
                result[num].append(density)
        result[num] = len(result[num])*(1/len(densities))
    return result

# EJERCICIO 8. Convertir un csv en json
def to_json(dataset):
# municipio_codigo;municipio_nombre;municipio_codigo_ine;nuts4_codigo;nuts4_nombre;superficie_km2;densidad_por_km2
    result = {"muns":[]}
    dict_keys = dataset[0]
    for mun in dataset[1:]:
        pre_dict = {}
        for i, key in enumerate(dict_keys):
            if i == 5 or i == 6:
                pre_dict[key] = float(mun[i])
            else:
                pre_dict[key] = mun[i]
        result["muns"].append(pre_dict)
    return result

with open("data_municipios.csv", mode="r", encoding="utf8") as file:
    data = list(csv.reader(file, delimiter=";"))
    # lo convertimos en lista para que se pueda sacar de la indentación del open
print(data)

# Ejercicio 1
mun_to_search = get_by_ine(data,"280014")
print(f"EJERCICIO 1: {mun_to_search}")

# Ejercicio 2
biggest_mun = get_biggest_mun(data)
print(f"EJERCICIO 2: {biggest_mun}")

# Ejercicio 3
sup_total = get_sup_total(data)
print(f"EJERCICIO 3: {sup_total}")

#Ejercicio 4
total_density = get_total_density(data)
print(f"EJERCICIO 4: {total_density}")

#Ejercicio 5
total_population = get_total_population(data)
print(f"EJERCICIO 5: {total_population}")

#Ejercicio 6
average_population = get_average_population(data)
print(f"EJERCICIO 6: {average_population}")

#Ejercicio 7
benford = benford(data)
print("EJERCICIO 7: ")
for k,v in benford.items():
    print(f"{k}: {v}")


#Ejercicio 8
dict_json = to_json(data)
with open("./municipios.json", mode="w",encoding="utf8") as file:
    json.dump(dict_json,file,indent=4,ensure_ascii=False)
        



        
            