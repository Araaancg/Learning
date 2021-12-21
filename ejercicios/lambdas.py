# Introducción a las funciones lambda

def saludar(name):
    return f"¡Hola {name}!"

lambda name: f"Hola {name}"

calculator = {
    "add": lambda a,b: a + b,
    "substract": lambda a,b: a - b,
    "square": lambda a: a**2,
    "cube": lambda a: a**3
}

# print(calculator["add"](3,5))


# GENERADORES map y filter

names = ["Marcelo", "Pedro", "German", "Alicia", "María", "Eusebio", "Rolando"]

names_m = list(filter(lambda name: name.startswith("M"), names))
print(names_m)



