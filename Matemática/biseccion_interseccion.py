"""
El programa encuentra la intersección de estas dos funciones y1 y y2, que se pueden modificar.
Utiliza el método de la bisección hasta alcanzar una estimación de la solución r, con una tolerancia de 0,0001. 
Presenta también una tabla con los siguientes valores: 
n (número de la iteración), 
an (extremo inferior del intervalo), 
bn (extremo superior del intervalo), 
cn (estimación de la raíz), 
f(an), f(bn) y f(cn).
"""

from biseccion import biseccion
import numpy as np

def y1(x):
    return np.sqrt(x**2 + 1)

def y2(x):
    return np.tan(x)

def diferencia_y1_y2(x):
    return y1(x) - y2(x)

a = 0.5
b = 1.0
tol = 0.0001

def biseccion(f, a, b, tol):
    if f(a) * f(b) >= 0:
        raise ValueError("El método de bisección no puede aplicarse. f(a) y f(b) deben ser de signos opuestos.")
    
    iteraciones = []
    c = (a + b) / 2
    
    for i in range(100):
        iteraciones.append((i, a, b, c, f(a), f(b), f(c)))
        
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    
    return c, f(c), abs(f(c)), iteraciones

c, fc, error, iteraciones = biseccion(diferencia_y1_y2, a, b, tol)

print('n = número de iteraciones',
      '\nan = extremo inferior del intervalo', 
      '\nbn = extremo superior del intervalo', 
      '\ncn = estimación de la raíz', 
      )

print(f"\n{'n':<5}{'an':<10}{'bn':<10}{'cn':<10}{'f(an)':<10}{'f(bn)':<10}{'f(cn)':<10}")

for i, a, b, c, fa, fb, fc in iteraciones:
    print(f"{i:<5}{a:<10.5f}{b:<10.5f}{c:<10.5f}{fa:<10.5f}{fb:<10.5f}{fc:<10.5f}")

print(f"\nLa raíz de la función es {c}, f(c) = {fc} y el error es {error}")

#####################3

import matplotlib.pyplot as plt

x = c
y = y1(x)
print(f"\nEl punto de intersección entre las dos funciones es ({x}, {y})")

x = np.linspace(0, np.pi/2, 1000)

y1_valores = np.sqrt(x**2 + 1)
y2_valores = np.tan(x)

plt.plot(x, y1_valores, label='y1 = sqrt(x^2 + 1)')
plt.plot(x, y2_valores, label='y2 = tan(x)')
plt.ylim([0, 5])  # esto es para limitar el rango de y para visualizar mejor
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()