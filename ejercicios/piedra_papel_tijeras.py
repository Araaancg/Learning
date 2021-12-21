#Juego de piedra papel tijeras

import random

options = ["piedra", "papel", "tijeras"] #opciones para elegir
print("Tienes tres opciones a elegir: piedra, papel o tijeras")

rounds = 0 #número de rondas
user_score = 0 #marcador del user
pc_score = 0 #marcador del pc

while rounds < 6:
    user = input("Elige la opcion que quieras de las tres: ")
    user_index = options.index(user)
    pc = random.choice(options)
    print(f"El pc ha elegido: {pc}") #imprimimos la opción del pc
    pc_index = options.index(pc)
    
    if pc_index == user_index:
        print("Empate")
        rounds -= 1 #se repite la ronda y el marcador se queda igual
    else: 
        if user_index == 2:
            if pc == 1:
                print("Has perdido")
                pc_score += 1
            else:
                print("Has ganado")
                user_score += 1
        else:
            if pc_index == user_index + 1:
                print("Has perdido")
                pc_score += 1
            else:
                print("Has ganado")
                user_score += 1
    rounds += 1

print(f"Marcador: user {user_score} - pc {pc_score}")