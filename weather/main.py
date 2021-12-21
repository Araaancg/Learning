'''
Aplicación del tiempo usando una url dinámica para que depende de la ciudad que pone el user sale 
una info u otra
En el menú hay que poner:
- Buscar por coordenadas, latitud y longitud
- Buscar por ciudad
- Buscar por ciudad y fecha *DE MOMENTO NO*

hacer lo de si mete un numero que no esta que de un mensaje erroneo y vuelva al menu
'''

import requests as req
import weather_functions as wf

options = ["1","2","3","4","q"]

user = "0"

while user.lower() != "q":
    wf.menu()
    user = input(": ")
    if user in options:

        # Buscar por ciudad
        if user == "1":
            user = input("Introduzca el nombre de una ciudad: ").lower()
            info_city = wf.get_forecast(user)
            if info_city: 
                print("-"*50)
                wf.pretty_print_list(info_city)
                print("-"*50)
            else:
                print("-"*50)
                print("Localización no encontrada en la base de datos")
                # print("-"*50)
            user = input("Presione enter para volver al menu principal ")
        
        # Buscar por coordenadas
        if user == "2":
            lattlong = input("Introduzca la latitud y la longitud deseadadeseada (latt,long): ")
            info_city = wf.get_forecast(lattlong, coords=True)  
            print("-"*50)
            wf.pretty_print_list(info_city)
            print("-"*50)
            user = input("Presione enter para volver al menú principal ")

        # Buscar por fecha y ciudad
        if user == "3":
            user = input("Introduzca el nombre de una ciudad: ").lower()
            date = input("A continuación introduzca la fecha (y/m/d): ")
            print("-"*50)
            info_city = wf.get_forecast(user,date=date)

            # Manejo del error
            if info_city:
                wf.pretty_print_dic(user,info_city,date)
            else:
                print("Datos no encontrados en la base de datos")
        
        if user == "4":
            city_1 = input("Introduza el origen: ")
            city_2 = input("Introduzca el destino: ")
            city_1_info = wf.get_forecast(city_1)
            city_2_info = wf.get_forecast(city_2)
            cities = [city_1_info,city_2_info]
            print("-"*50)
            travel_planning = wf.plan_trip(city_1,city_2)
            wf.warning_bad_weather(cities)
            if travel_planning:
                print(f"Distancia entre {city_1.capitalize()} y {city_2.capitalize()}: {travel_planning[1]}")
                print(f"Duración del viaje: {travel_planning[0]}")
                print("-"*50)
            else: 
                print("Datos no encontrados en nuestra base")
            user = input("Presione enter para volver al menú principal ")

    else: # Input en el menú inválido
        print("Input inválido, por favor introduzca de nuevo la opción deseada")
        
print("Hasta pronto!")



'''
Nueva parte del programa: VIAJES

La misma permitirá elegir un origen y un destino e indicará, en base al clima lo siguiente:
- Aviso de mal clima (sn, sl, h, t hr)
- Distancia a recorrer (km.)
- Duración del trayecto (100 km/h)
- Si la velocidad del viento supera los 10 nudos, reducir la velocidad media a 90 km/h
'''