# introducir una contraseña y comprobar que cumple los requisitos
#Requisitos: 8 caráteres, al menos una letra, un número y sin espacios
'''
pwd = input("A continuación introduzca por favor una contraseña: ")

if pwd.isalnum() and not pwd.isnumeric() and not pwd.isalpha():
    print("Contraseña válida")
else:
    print("Contraseña inválida, pruebe con otra")
'''

#Considerando la variable a, sustituir las vocales por los números del 1 al 5

a = "murcielago"
a_num = a.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
print(a_num)

#Añadir a a la palabra kwargs tantas veces como carácteres tenga

a_mod = a + "kwargs" * len(a)
print(a_mod)

#Si lo anterior tiene un nº de caracteres impar obtener el caracter de en medio, sino añadir 75 al final

if len(a_mod) % 2 == 0:
    a_mod += "75"
    print(a_mod)
else:
    c_mitad = a_mod[int(len(a_mod)/2)]
    print(c_mitad)


