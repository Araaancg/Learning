#Averiguar la letra del dni

print("Este prgrama averiguará la letra de tu dni")

dni_sinletra = input("Ponga únicamente los numeros de su dni: ")
letras_dni = "TRWAGMYFPDXBNJZSQVLCKE"
resto_23 = int(dni_sinletra) % 23

# print(type(resto_23))

print(letras_dni[resto_23])