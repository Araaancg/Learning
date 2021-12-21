#Funciones para la app de la librería

#Base de datos libros

import csv
import datetime as dt


user = "0"

def csv_to_dict(data_base):
    with open("data.csv", mode="r") as file:
        csv_reader = csv.reader(file, delimiter=";")
        next(csv_reader)
        for i, row in enumerate(csv_reader):
            book = {
                "id": row[0],
                "title": row[1],
                "author":row[2],
                "genre":row[3]
            }
            data_base.append(book)


def export_db(data_base, file_export):
    with open(file_export, mode="w") as file:
        csv_writer = csv.writer(file, delimiter=";")
        csv_writer.writerow(["id","title","author","genre"])
        for book in data_base: 
            csv_writer.writerow(book.values())

def menu():
    print("1. Buscar por id")
    print("2. Buscar por título")
    print("3. Buscar por autor")
    print("4. Buscar por género")
    print("5. Actualizar registro")
    print("6. Eliminar un libro de la base de datos")
    print("7. Añadir un libro a la base de datos")
    print("8. Consultar la base de datos completa")
    print("Q. Terminar programa")
    print("-"*50)
    # Las nuevas opciones hay que añadirlas a la lista de options 

def menu_remove():
    print("WARNING! ¿Quiere eliminar este libro?")
    print("1. Continuar con la acción")
    print("2. Escoger otro libro a eliminar")
    print("3. Cancelar acción")

def get_by_term(term, term2search, data_base):
    books_found = []
    for book in data_base:
        if book[term].lower().find(term2search.lower()) >= 0:
            books_found.append(book)
    return books_found

def remove_book(book, data_base):
    data_base.remove(book)

def write_excel(data_base):
    with open("data.csv", mode="a", encoding="utf8") as file:
        csv_writer = csv.writer(file, delimiter=";")
        csv_writer.writerow(["id","title","author","genre"])
        for book in data_base: 
            csv_writer.writerow(book.values())

def update_book(book,genre_list):
    print("Reescriba la información a su gusto\nPresione enter en lo que no quiera modificar\n")
    for k,v in list(book[0].items())[1:3]:
        user = input(f"{k.capitalize()}: ")
    if user:    
            book[0][k] = user
    print("Escoga un género: ")
    print("0. Añadir un género nuevo")
    for i, genre in enumerate(genre_list):
        print(f"{i+1}. {genre}")
    user = input(": ")
    if user:
        while int(user) not in [num for num in range(0, len(genre_list))]:
            print("Número no válido, vuelva a elegir")
            user = input(": ")
        if user == "0":
            book[0]["genre"] = input("Introduzca el nuevo género: ")
        elif int(user) <= len(genre_list) and int(user) > 0:
            book[0]["genre"] = genre_list[int(user)-1]

        

def add_book(data_base,genre_list):
    print("NUEVO LIBRO\n")
    new_book_id = input("Id: ")
    new_book_title = input("Title: ")
    new_book_author = input("Author: ")
    new_book_genre = None
    print("Elija un género: ")
    print("0. Añadir un género nuevo")
    for i, genre in enumerate(genre_list):
        print(f"{i+1}: {genre}")
    user = input(": ")
    if user == "0":
        new_book_genre = input("\nIntroduzca el nuevo género: ")
    elif int(user) <= len(genre_list) and int(user) > 0:
        new_book_genre = genre_list[int(user)-1]
    else:
        print("Número no válido, género inexistente")
        new_book_genre = "Inexistente" 
    new_dict = {
        "id": new_book_id,
        "title": new_book_title,
        "author": new_book_author,
        "genre": new_book_genre
    }
    data_base.append(new_dict)
    return new_dict

def pretty_search_book(lista):
    print("-"*50)
    print("LIBRO(S) ENCONTRADO(S)")
    print(" ")
    for book in lista:
        for k, v in book.items():
            print(f"{k.capitalize()}: {v}")
        print(" ")

def pretty_book(lista):
    for book in lista:
        for k, v in book.items():
            print(f"{k.capitalize()}: {v}")
        print(" ")

def generar_lista(term, database):
    lista = []
    for book in database:
        if book[term] not in lista:
            lista.append(book[term])
    return lista

def history(lista, sentence):
    for book in lista:
        with open("./history.log", mode="a", encoding="utf8") as file:
            file.write(f"{dt.datetime.now()} | {sentence}: {book}\n")