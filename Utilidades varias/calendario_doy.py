# El siguiente programa permite obtener el día del año (DOY) a partir de una fecha ingresada por el usuario.

def anio_bisiesto(anio):
    if anio % 4 == 0:
        return True
    elif anio % 4 == 0 and anio % 100 != 0:
        return True
    elif anio % 100 == 0 and anio % 400 != 0:
        return False
    elif anio % 100 == 0 and anio % 400 == 0:
        return True
    
def doy(dia, mes, anio):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if anio_bisiesto(anio): # si el año es bisiesto, febrero tiene 29 días
        dias_mes[1] = 29 
    doy = dia # se empieza con el día ingresado 
    for i in range(mes-1): # se recorren los meses anteriores al ingresado
        doy = doy + dias_mes[i] # se suman los días de los meses anteriores. Es lo mismo que hacer doy += dias_mes[i]
    return doy

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
print("El día {} del mes {} del año {} corresponde al día {} del calendario DOY".format(dia, mes, anio, doy(dia, mes, anio)))