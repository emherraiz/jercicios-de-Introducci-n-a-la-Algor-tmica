# El IRPF lo vamos a dejar predefinido mediante la siguiente función:
def IRPF(Precio, Ganancias):
    '''Tramos del IRPF'''
    if 0 < Ganancias < 12450:
        irpf = .19
    elif 12450 <= Ganancias < 20200:
        irpf = .24
    elif 20200 <= Ganancias < 35200:
        irpf = .3
    elif 35200 <= Ganancias < 60000:
        irpf = .37
    elif 60000 <= Ganancias < 300000:
        irpf = .45
    elif 300000 < Ganancias:
        irpf = .47
    else:
        irpf = 0

    return Precio - (Ganancias*irpf)

# Precio de nuestro producto sobre el que aplicaremos directamente el IVA
Precio = float(input('Introduce el precio de nuestro producto'))

# Definimos el tipo de IVA según nuestro producto
Opcion = 0
while Opcion not in range(1, 5):
    Opcion = int(input('Selecciona el tipo de IVA que quieres aplicar:\n 1 - 21%\n 2 - 10%\n 3 - 4%\n 4 - Sin IVA'))
if Opcion == 1:
    Iva = .21
elif Opcion == 2:
    Iva = .1
elif Opcion == 3:
    Iva = .04
else:
    Iva = 0

# Los intereses y el tiempo nos darán ganancias sobre las cuales aplicaremos cada año el IRPF
Interes = float(input('Introduce el interés mensual en tanto por ciento que recibe nuestro producto'))
Tiempo = int(input('Tiempo que mantenemos nuestra inversión'))

Precio_de_partida = Precio
Precio_temp = Precio - (Precio*Iva)
Precio = Precio_temp
for i in range(Tiempo):
    Precio = Precio + (Precio*(Interes/100))
    if i % 12 == 0:
        Ganancias = Precio - Precio_temp
        Precio = IRPF(Precio, Ganancias)
        Precio_temp = Precio
print(f'El precio final es de {round(Precio, 2)}')
print(f'Obteniendo un beneficio de {round(Precio - Precio_de_partida, 2)}')
