# El siguiente código toma como entrada el DOY y el año y reporta a qué día y mes calendario corresponde.

from calendario_doy import anio_bisiesto

def fecha(doy, anio):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if anio_bisiesto(anio):
        dias_mes[1] = 29
    mes = 1
    while doy > dias_mes[mes-1]:
        doy -= dias_mes[mes-1]
        mes += 1
    return doy, mes

doy = int(input("Ingrese el día del año: "))
anio = int(input("Ingrese el año: "))
dia, mes = fecha(doy, anio)
print("El día del año {} del año {} corresponde al día {} del mes {}".format(doy, anio, dia, mes))