# Proyecto pokemon, empezando con objetos

from os import system
import time
from random import choice

elements = ["fire","water","grass"]

class Pokemon:
    def __init__(self,name,element,HP):
        self.name = name
        self.element = element
        self.HP = [HP,HP] #La primera es la que se verá afectada en las batallas
        self.is_alive = True
        self.attacks = []

    def learn(self, attack):
        self.attacks.append(attack)

    def receive_damage(self,attack):
        self.HP[0] -= attack.damage
        self.is_alive = True if self.HP[0] > 0 else False

    def __str__(self):
        return f"Pokemon({self.name},{self.element},{self.HP})"
   
class Attack:
    def __init__(self,name,element,damage):
        self.name = name
        self.element = element
        self.damage = damage
    
    def __repr__(self):
        return f"Attack({self.name},{self.element},{self.damage})"


# POKEMONS
charmander = Pokemon("Charmander",elements[0],100.0)
squirtle = Pokemon("Squirtle",elements[1],100.0)
bulbasur = Pokemon("Bulbasur",elements[2],100.0)
pokemons = [charmander,squirtle,bulbasur]

#ATAQUES
# Ataques de FUEGO
flamethrower = Attack("Flamethrower",elements[0],20.0)
fireball = Attack("Fireball",elements[0],25.0)
dragon_fury = Attack("Dragon fury",elements[0],30.0)
#Ataques de AGUA
explosive_bubble = Attack("Explosive bubble",elements[1],20.0)
aqua_tail = Attack("Aqua tail",elements[1],25.0)
tsunami = Attack("Tsunami",elements[1],30.0)

all_attacks = [flamethrower,fireball,dragon_fury,explosive_bubble,aqua_tail,tsunami]

#Pokemons aprenden ataques
for pokemon in pokemons:
    for attack in all_attacks:
        if pokemon.element == attack.element:
            pokemon.learn(attack)

separador = "-"*30

def menu():
    print("-"*30)
    print("BATALLA POKEMON".center(30))
    print("1. Charmander")
    print("2. Squirtle")
    print("Q. Terminar programa")
    print("-"*30)

def attack_menu(pokemon):
    for i,attack in enumerate(pokemon.attacks):
        print(f"{i+1}. {attack.name}")
    
def battle(choosen_poke,oponent):
    system("clear")
    oponent.HP[0], oponent.is_alive = oponent.HP[1], True
    choosen_poke.HP[0], choosen_poke.is_alive = choosen_poke.HP[1], True
    while oponent.is_alive and choosen_poke.is_alive:
        print(" ")
        print(f"{choosen_poke.name.capitalize()}: {choosen_poke.HP[0]}          {oponent.name.capitalize()}: {oponent.HP[0]}")
        attack_menu(choosen_poke)

        #ATAQUES
        choosen_attack = choosen_poke.attacks[int(input(": "))-1] #Elegimos el ataque
        oponent.receive_damage(choosen_attack) #Atacamos nostros (choosen_poke)
        oponent_attack = choice(oponent.attacks) #El oponente (pc) elige un ataque
        choosen_poke.receive_damage(oponent_attack) #El oponente ataca

        print(f"{choosen_poke.name} --> {choosen_attack.name} -{choosen_attack.damage} pts")
        print(f"{oponent.name} --> {oponent_attack.name} -{oponent_attack.damage} pts")
        time.sleep(1)
        system("clear")

    if oponent.is_alive:    
        print(f"{separador}\n{choosen_poke.name.capitalize()} se ha desmayado\nTú y {choosen_poke.name.capitalize()} habeís PERDIDO la batalla\n{separador}")
    else:
        print(f"{separador}\n{oponent.name.capitalize()} se ha desmayado\nTú y {choosen_poke.name.capitalize()} habeis GANADO la batalla\n{separador}")

user = ""

while user.lower() != "q":
    menu()
    user = input(": ")
    print("-"*30)

    if user == "1": #Elije a charmander
        choosen_poke = charmander
        oponent = squirtle
        print(f"Has elegido a {choosen_poke.name.upper()} y tu oponente es {oponent.name.upper()}")
        battle(choosen_poke,oponent)
        input("Presiona enter para volver al menú ")

    if user == "2": #Elije a squirtle
        choosen_poke = squirtle
        oponent = charmander
        print(f"Has elegido a {choosen_poke.name.upper()} y tu oponente es {oponent.name.upper()}")
        time.sleep(1)
        battle(choosen_poke,oponent)
        input("Presiona enter para volver al menú ")

print("¡Hasta pronto!")




