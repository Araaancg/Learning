import json
from hashlib import sha256

DB = "./users.json"


def get_users(json_file):
    with open(json_file,encoding="utf8") as file:
        return json.load(file)

def create_user(data, json_file):
    with open(json_file,"w",encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

user = ""
while user != "q":
    print("1. Crear usuario")
    print("2. Log in")
    print("Q. Terminar programa")
    user = input(": ")
    if user == "1":
        user_name = input("Name: ")
        user_pwd = input("Password: ")
        pwd_e_bytes = sha256(user_pwd.encode())
        pwd_e_str = pwd_e_bytes.hexdigest()
        users = get_users(DB)
        users["data"].append({"name": user_name, "pwd": pwd_e_str})
        create_user(users, DB)
    