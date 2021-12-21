import requests as req
import json
import random

def menu():
    print("-"*30)
    print("LOS PAÍSES".center(30))
    print("1. Buscar información de un país")
    print("2. Descargar la bandera de un país")
    print("3. Jugar")
    print("Q. Terminar programa")
    print("-"*30)

def get_by_term(c, **kwargs):
    term = "name"
    if kwargs.get("continent"):
        term = "region"
    c_info = req.get(f"https://restcountries.com/v3.1/{term}/{c}").json()  
    try:
        country_info["status"]
        return None
    except:
        return c_info

def pretty_print(country_info):
    print(country_info[0]["name"]["common"].upper().center(30))
    print(f"       Capital: {country_info[0]['capital'][0]}")
    print(f"     Población: {country_info[0]['population']} habitantes")
    print(f"    Superficie: {country_info[0]['area']} km2")
    languages = list(country_info[0]['languages'].values())
    print(f"        Idioma: {languages}")

# def choose_continents():
#     continents = ["Asia","Europe","Oceania","Africa","Americas"]
#     print("Continentes".center(30))
#     for i, continent in enumerate(continents):
#         print(f"{i+1}: {continent}")
#     user = input("Elija un continente: ")
#     if int(user) > 0 and int(user) <= len(continents):
#         user_cont = continents[int(user)-1]
#         return user_cont.lower()
#     else:
#         return None 

# choose_continents()


#########################################################################
#QUIZ
# def countries_list(raw_list): #Pasamos la lista del json y la amoldamos a los datos que vamos a usar
    # countries = list(map(lambda country: {
    #     "name":country["name"]["common"],
    #     # "capital":country['capital'],
    #     "capital":country.get("capital"[0]),
    #     "area":country["area"],
    #     "drive_side":country["car"]["side"],
    #     "population":country["population"]
    # },raw_list))
    # return countries


def quiz(countries,continent):   #continent = nombre del continente elegido(str), countries = lista de país del continent(list)
    count = 1
    score = 0

    while count <= 5: #Hacemos 5 preguntas
        print(f"Pregunta {count}") # Ponemos el número de pregunta para que el user sepa cuantas lleva
        ch_co = random.choice(countries) # Se reinicia la chosen country
        quiz = [
            {
                "q":f"Capital de {ch_co['name']}",
                "a":ch_co['capital'],
                "o":[random.choice(countries)['capital'], random.choice(countries)['capital'],ch_co['capital']]
            },
            {
                "q":f"Población de {ch_co['name']}",
                "a":ch_co['population'],
                "o":[random.choice(countries)['population'], random.choice(countries)['population'],ch_co['population']]
            },
            {
                "q":f"Por que lado conducen en {ch_co['name']}",
                "a":ch_co['drive_side'],
                "o":["right","left"]
            },
            {
                "q":f"Cuantos países hay en {continent}",
                "a": len(countries),
                "o":[len(countries)-11,len(countries)+6,len(countries)]
            }
        ]

        question = random.choice(quiz)
        print(question.get("q")) # Imprimimos la pregunta

        answers = [answer for answer in question["o"]]
        random.shuffle(answers) # Mezclamos las respuestas 

        for i,answer in enumerate(answers): #Imprmimos las respuestas 
            print(f"{i+1}. {answer}")
        user = input(": ").lower() #El usuario pondrá un nº del 1 hasta el len(answers)

        if answers[int(user)-1] == question["a"]: #Comprobamos si es correcta la respuesta
            print("Respuesta correcta")
            score += 1
        else:
            print("Respuesta incorrecta")

        count += 1 #Número de preguntas +1

    print(f"Has acertado {score}/5")