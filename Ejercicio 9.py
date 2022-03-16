def media(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma / len(lista)

def crearlista():
    n = int(input('Tamaño de nuestra lista'))
    lista = []
    print(f'Introduce {n} números a la lista:')
    for i in range(n):
        lista.append(float(input(f'{i+1} - ')))
    return lista
lista = crearlista()
print(lista)
print(f'La media es {media(lista)}')

def mediaponderada(lista, ponderadas):
    lista_final = []
    for i in range(len(lista)):
        lista_final.append(lista[i]*ponderadas[i])
    return media(lista_final)

opcion = input('Si desea crear una nueva lista pulse s')
if  opcion == 's':
    crearlista()
ponderadas = []
print('Ahora vamos a introducir los coeficientes de ponderación de cada valor')
for i in range(len(lista)):
    ponderadas.append(float(input(f'{i+1} - El coeficiente de ponderación de {lista[i]} es'))) 
# En el caso de que lo dieramos en tanto por ciento simplemente habría que dividirlo entre 100 cada uno de los valores

print(f'Nuestra media ponderada es {mediaponderada(lista, ponderadas)}')
