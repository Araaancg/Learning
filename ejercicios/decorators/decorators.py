# Introduction to decorators

# EJERCICIO 1: agregar una función que retorne "hola" con un signo de exclamación
def exclamation(func_to_decorate):
    def inner():
        return f"¡{func_to_decorate()}!"
    return inner

@exclamation
def greeting():
    return "Hola"

print(F"\nEJERCICIO 1: {greeting()}\n")


# EJERCICIO 2: agregar un decor que retorne la función en mayúsculas
def upper_case(func_to_decorate):
    def inner():
        return func_to_decorate().upper()
    return inner

@exclamation # Se puede poner más de un decorator
@upper_case
def regards():
    return "Chau"

print(f"EJERCICIO 2: {regards()}\n")

# EJERCICIO 3: crear un decorador log que agrege en el fichero logs el nombre de la función y la hora de ejecución
import datetime as dt

def log(func_to_decorate):
    def inner():
        info = f"{dt.datetime.now()} | {func_to_decorate.__name__}\n"
        with open("./calls.log",mode="a",encoding="utf8") as file:
            file.write(info)
        return func_to_decorate()
    return inner

@exclamation 
@log # Importante ponerlo abajo de todos los decoradores porque sino te hace el log del decorador anterior (en este caso @exclamation)
def congrats():
    return "Felicidades"

print("EJERCICIO 3:")
print(f"{congrats()}\n")