# se solicitarán en pantalla los coeficientes (a, b y c) de un polinomio de segundo grado y se mostrarán las raíces 
# del polinomio ingresado.

import numpy as np

def calcular_polinomio(a, b, c):
    x1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

a = float(input("Ingrese el coeficiente A: "))
b = float(input("Ingrese el coeficiente B: "))
c = float(input("Ingrese el coeficiente C: "))

raiz1, raiz2 = calcular_polinomio(a, b, c)

print("El polinomio ingresado es: {}x^2 + {}x + {}".format(a, b, c))
print("Las raíces del polinomio son: {} y {}".format(raiz1, raiz2))