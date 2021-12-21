import requests as req
import random
import c_functions as cf

# Quiz aquí para que sea más manejable

# Nos dan el continente, el nombre
# Continentes: Africa, Asia, Americas, Oceania, Europa
#Hacemos request para traernos de primeras la api del continente, lo hacemos filtrando la info que necesitamos
continent = "Europe"
# continent = cf.choose_continents()
url = "https://restcountries.com/v3.1/region/"
res = req.get(url+continent).json()
countries = list(map(lambda country: {
    "name":country["name"]["common"],
    "capital":country["capital"][0],
    "area":country["area"],
    "drive_side":country["car"]["side"],
    "population":country["population"]
},res))

# print(res)
# print("_"*30)
# print(countries)

count = 1
score = 0


while count <= 5:
    print(f"Pregunta {count}") # Ponemos el número de pregunta para que el user sepa cuantas lleva
    ch_co = random.choice(countries) # Se reinicia la chosen country
    # print(ch_co)
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
