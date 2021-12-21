m_course = [{
	"name": "Patricia",
	"id" :  "001",
    "score": 8.1
},
{
	"name": "Nicole",
	"id" :  "002",
    "score": 6.6
},
{
	"name": "Javier",
	"id" :  "003",
    "score": 10
},
{
	"name": "Verónica",
	"id" :  "004",
    "score": 8.6
},
{
	"name": "Guillermo",
	"id" :  "005",
    "score": 4
},
{
	"name": "Pablo",
	"id" :  "006",
    "score": 9
},
{
	"name": "Patricia",
	"id" :  "007",
    "score": 2.3
}
]

a_course =[
{
	"name": "Germán",
	"id" :  "001",
    "score": 6.8
},
{
	"name": "Sara",
	"id" :  "002",
    "score": 8.8
},
{
	"name": "Jorge",
	"id" :  "003",
    "score": 3.3
},
{
	"name": "María",
	"id" :  "004",
    "score": 9.8
},
{
	"name": "Alicia",
	"id" :  "005",
    "score": 5.6
},
{
	"name": "Hernesto",
	"id" :  "006",
    "score": 6.8
}]

courses = a_course + m_course

#Obtener la nota de Hernesto, sin importar como se escriba en el input

student_to_find = "Hernesto"
#student_to_find = input()

for student in courses:
    if student["name"].lower() == student_to_find.lower():
        print(student["name"],student["score"])

#Estudiantes cuyo nombre empieze por la letra "P"

count = 0

for student in courses:
    if student["name"].lower().startswith("p"):
        count += 1
print(f"Hay {count} estudiantes cuyo nombre empieza por la 'p'")


#Nombre de la/el estudiantes con la nota más alta

highest_score = 0
student_with_high_score = ""

for student in courses:
    if student["score"] > highest_score:
        highest_score = student["score"]
        student_with_high_score = student["name"]

print(f"{student_with_high_score} tiene la nota más alta, siendo esta un {highest_score}")

#Nombre de la/el estudiantes con la nota más baja

lowest_score = 10
student_with_low_score = ""

for student in courses:
    if student["score"] < lowest_score:
        lowest_score = student["score"]
        student_with_low_score = student["name"]

print(f"{student_with_low_score} tiene la nota más baja, siendo esta un {lowest_score}")


#Modificar la nota de Alicia a un 6.7 (también se puede hacer con inputs)

modif_student = "Alicia"
modif_score = 6.7

for student in courses:
    if student["name"].lower() == modif_student.lower():
        student["score"] = modif_score

print(f"La nota de {modif_student} se ha cambiado a un {modif_score}")

#Agregar a los estudiantes de la lista m_course la letra M delante del id

for student in m_course:
    student["id"] = "M" + student["id"]
    #print(student["id"])
    
    
#Agregar a los estudiantes de la lista a_course la letra A delante del id

for student in a_course:
    student["id"] = "A" + student["id"]
    #print(student["id"])

#Crear dos listas, una con estudiantes aprobados y otra con estudiantes suspensos

lista_aprobados = []
lista_suspensos = []

for student in courses:
    if student["score"] > 6:    #Por norma el 6 es la nota mínima para aprobar
        lista_aprobados.append(student)
    else:
        lista_suspensos.append(student)
    
# print("                                           ")
# print(f"La lista de aprobados es {lista_aprobados}")
# print("                                           ")
# print(f"La lista de suspensos es {lista_suspensos}")

print(courses)