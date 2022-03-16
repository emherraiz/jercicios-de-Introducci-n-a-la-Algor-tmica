def area(base, altura):
    return base*altura/2

base = float(input('Medida de un lado'))
altura = float(input('Altura relativa a ese lado'))
print(f'El area del triángulo es de {area(base, altura)} unidades')
