#simular el método count con bucle while


repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]

num_to_search = 2
i = 0 #índice de los diferentes elementos de la lista
count = 0 #las veces que sale el num to search

'''
while i < len(repeated_numbers):
    print(repeated_numbers[i])
    if repeated_numbers[i] == num_to_search:
        count += 1
    i += 1

print(f"num_to_search is repeated {count} times")
print(repeated_numbers.count(2))
'''


#simular el método count con el bucle for

'''
for num in repeated_numbers:
    if num_to_search == num:
        count += 1
    i += i
print(count)
'''


#simular el método index con el bucle while

'''
while i < len(repeated_numbers):
    if num_to_search == repeated_numbers[i]:
        print(i)
        break #estructura de control para romper el bucle 
    i += 1

print(repeated_numbers.index(2))
'''


#simular el método count con el bucle for

'''
for num in repeated_numbers:
    if num_to_search == num:
        print(i)
        break #estructura de control para romper el bucle
    i += 1
'''


#hacer un iterable de repeated_numbers en el cual no haya ningun valor repetido


repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]
lista_nueva = [] #lista donde añadimos los nuevos valores

#forma más fácil
'''
for num in repeated_numbers:
    if num not in lista_nueva:
        lista_nueva.append(num)
print(lista_nueva)
'''


#hacerlo con count
'''
for num in repeated_numbers:
    if repeated_numbers.count(num) == 1:
        lista_nueva.append(num)
    else:
        if lista_nueva.count(num) == 0:
            lista_nueva.append(num)
print(lista_nueva)
'''

#hacerlo con set, más fácil aún
'''
result = set(repeated_numbers) 
print(result) #además de solucionar el ejercicio, ordena los números
'''

# En el mismo bucle crear dos listas, una con los valores pares y otra con impares


repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]
lista_par = []
lista_impar = []

'''
for num in repeated_numbers:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)    

print(f"LISTA PAR: {lista_par}")
print(f"LISTA IMPAR: {lista_impar}")
'''


# Crear una lista resultante con los valores de repeated_mnumbers al cuadrado


repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]
lista_alcuadrado = []
'''
for num in repeated_numbers:
    lista_alcuadrado.append(num**2)

print(f"LISTA AL CUADRADO: {lista_alcuadrado}")
'''

#Obtener la media

'''
i = 0
sum = 0
for num in repeated_numbers:
    sum += repeated_numbers[i]
    i += 1

print (sum)
media = sum/len(repeated_numbers)
print(media)
'''

#Obetener el valor máximo y cambiarlo 1000

'''
num_max = 0

for num in repeated_numbers:
    if num > num_max:
        num_max = num

print(num_max)

repeated_numbers[repeated_numbers.index(num_max)] = 1000
print(repeated_numbers)
'''

#Obtener la sumatoria de los valores comprendidos entre las posiciones 4 y 9

repeated_numbers = [1,2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98]
lista_sumatoria4_9 = 0

'''
for num in repeated_numbers:
    if 4 <= i <= 10:
        lista_sumatoria4_9 += num
    i += 1

for i, num in enumerate(repeated_numbers):
    if 4 <= i <= 10:
        lista_sumatoria4_9 += num

print(lista_sumatoria4_9)

lista_sumatoria4_9_vito = sum(num for i, num in enumerate(repeated_numbers) if i>= 4 and i<=10)
print(lista_sumatoria4_9_vito)
'''

# Crear 15 números de la lista de Fibonacci

fibonacci = [1,1]
i = 0

while i < 15:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
    i += 1

print(fibonacci)





