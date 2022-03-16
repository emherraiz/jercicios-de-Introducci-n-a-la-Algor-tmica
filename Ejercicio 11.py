salario = float(input('Introduce el salario mensual bruto'))
horas_extra = int(input('Cantidad de horas extras trabajadas'))
sueldo_por_hora = salario*12/(52*35)
importe_extra = 0
if horas_extra > 0:
    for i in range(horas_extra):
        if 0 <= i <= (43 - 35):
            importe_extra += sueldo_por_hora * 1.25
        else:
            importe_extra += sueldo_por_hora * 1.5

print(f'Al salario anual de {salario*12} € se le tiene que añadir una tarifa de {round(importe_extra, 2)} € por la cantidad de {horas_extra} horas extra trabajadas')
