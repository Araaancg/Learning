# AUTHENTIFICATION

import json

user = ""

def get_data(json_file):
    with open(json_file,encoding="utf8") as file:
        return json.load(file)
    
data = get_data("users.json")
print(data)

def create_user(name,passw):
    user = {}
    user["name"] = name
    user["password"] = passw
    data["users"].append(user)
        

while user.lower() != "q":
    print("1. Crear usuario")
    print("2. Log in")
    print("Q. Terminar programa")
    user = input(": ")

    if user == "1":
        user = input("Elija un nombre de usuario: ")
        password = input("Escriba una contraseña: ")
        create_user(user,password)


with open("./users.json", mode="w",encoding="utf8") as file:
    json.dump(data,"users.json",indent=4) 