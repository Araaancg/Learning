'''
Aquí estarán las funciones de la app del weather

A mostrar:
- La descripción del tiempo (nuboso, soleado...)
- La temp max y min
- Sensación térmica
- Humedad
- Velocidad del viento
'''
import requests as req
import json

weather_abbreviation_dic = {
    "lr":"Light Rain",
    "hr":"Heavy Rain",
    "h":"Hail",
    "sn":"Snow",
    "sl":"Sleet",
    "t":"Thunderstorm",
    "s":"Showers",
    "hc":"Heavy Cloud",
    "lc":"Light Cloud",
    "c":"clear"
}

def get_data(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)

woeids_dic = get_data("woeids.json")  # Diccionario para poder evitar una request y así ahorrar tiempo

def write_data(data,json_file):
    with open(json_file, mode="w",encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def menu():
    print("-"*50)
    print("EL TIEMPO".center(50))
    print("1. Buscar por ciudad")
    print("2. Buscar por coordendadas (latitud,longitud)")
    print("3. Buscar el tiempo de una ciudad por fecha")
    print("4. Planea tu viaje")
    print("Q. Terminar programa")
    print("-"*50)


def get_forecast(location, **kwargs):
    # PRIMER PASO: encontrar el woeid
    term = "query"
    woeid = woeids_dic.get("location") # Lo buscamos en el diccionario de woeids
    if not woeid:
        if kwargs.get("coords"):
            term = "lattlong"

        try: # Manejo de errores al consultar a la base de datos
            request = req.get(f"https://www.metaweather.com/api/location/search/?{term}={location}").json()
        except:
            return None

        # Meter todos los woeids posibles en el dicc
        for city in request:
            woeids_dic[city["title"].lower()] = city["woeid"]
            write_data(woeids_dic,"woeids.json")
        woeid = request[0]["woeid"]
    
    # SEGUNDO PASO: buscar la info de la ciudad
    url = f"https://www.metaweather.com/api/location/{woeid}/"
    if kwargs.get("date"): # Si nos dan una fecha se añade a la url. Formato = year/month/day
        url += kwargs.get("date")
    try: # Manejo de errores al consultar a la base de datos
        request = req.get(url).json()
    except:
        return None
    return request


def pretty_print_list(city_list): # Para cuando me pasan una lista
    print(city_list['title'].upper().center(45))
    print(f"Descripción del tiempo: {city_list['consolidated_weather'][0]['weather_state_name']}")
    print(f"    Temperatura máxima: {city_list['consolidated_weather'][0]['max_temp']}°")
    print(f"    Temperatura mínima: {city_list['consolidated_weather'][0]['min_temp']}°")
    print(f"     Sensación térmica: {city_list['consolidated_weather'][0]['the_temp']}°")
    print(f"               Humedad: {city_list['consolidated_weather'][0]['humidity']} %")
    print(f"  Velocidad del viento: {city_list['consolidated_weather'][0]['wind_speed']} m/s")


def pretty_print_dic(city_name, city_list, date): # Para cuando me pasan un diccionario (al buscar por fecha)
    print(f"{city_name.upper()}   {date}".center(50))
    print(f"Descripción del tiempo: {city_list[0]['weather_state_name']}")
    print(f"    Temperatura máxima: {city_list[0]['max_temp']}°")
    print(f"    Temperatura mínima: {city_list[0]['min_temp']}°")
    print(f"     Sensación térmica: {city_list[0]['the_temp']}°")
    print(f"               Humedad: {city_list[0]['humidity']} %")
    print(f"  Velocidad del viento: {city_list[0]['wind_speed']} m/s")

def warning_bad_weather(city_list):
    bad_weather = ["sn","sl","h","t","hr","lr"]
    # sn = snow, sl = sleet, h = hail, t = thunderstorm, hr = heavy rain, lr = light rain
    for city in city_list:
        prediction_weather = city["consolidated_weather"][0]["weather_state_abbr"]
        city_name = city["title"]
        if prediction_weather in bad_weather:
            weather_state = weather_abbreviation_dic[prediction_weather]
            print(f"WARNING: en {city_name} va a hacer mal tiempo ({weather_state})")
        # else:
        #     print(f"Yay, en {city_name} va a hacer buen tiempo")

def plan_trip(city_1,city_2):
    # PRIMER PASO: Buscamos las coordenadas de la ciudad origen
    try: # Of course manejo de errores :)
        request = req.get(f"https://www.metaweather.com/api/location/search/?query={city_1}").json()
        coords = request[0]["latt_long"]

        # Buscamos las coords de nuevo para que salga la lista de ciudades "cercanas"
        request = req.get(f"https://www.metaweather.com/api/location/search/?lattlong={coords}").json()

        # SEGUNDO PASO: Metemos los nuevos woeids en el diccionario porque nunca seran suficientes
        # ya de paso usamos el bucle para buscar la city_2 y en su defecto la distancia
        distance = 0
        for city in request:
            woeids_dic[city["title"].lower()] = city["woeid"]
            write_data(woeids_dic,"woeids.json")
            if city["title"].lower() == city_2:
                distance = city["distance"]

        # TERCER PASO: calculamos el tiempo en base al viento de la ciudad origen (i guess)
        woeid = request[0]["woeid"]
        # con el woeid requesteamos (+ manejo de errores) la lista del weather
        request = req.get(f"https://www.metaweather.com/api/location/{woeid}/").json()
        velocity = 100 #km/h por defecto
        if request['consolidated_weather'][0]['wind_speed'] >= 10: 
            velocity = 90 #km/h cambiamos la velocidad si hay mucho viento

        #v=d/t --> t=d/v
        time = (int(distance)/velocity)/1000

        return time,distance

    except:
        return None


'''
Añadir lo de que te salgan los pronósticos de los tres siguientes dias, no sé si hacerlo 
una opción voluntaria a gusto del consumidor o que se joday que le salga siempre
Añadir también lo de los viajes, con lo de las distancias etc
meter en lo que llevo de los viajes manejo del error, en el warning digo

me voy a divertir mañana si

si ya me da tiempo, que obviamente no tiene pinta, añadir un while para que si se equivoca
al añadir la ciudad pues que no vuelva al menú principal, vamos a darle al user otra
oportunidad

ya si encima me aburro mucho añadir lo de ciudades favoritas

ambiciosa me llamaban 

genovese.work@gmail.com
genovese.work@protonmail.com

'''