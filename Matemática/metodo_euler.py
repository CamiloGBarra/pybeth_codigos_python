import numpy as np
import matplotlib.pyplot as plt

def metodo_euler(f, t0, tf, x0, h):
    # Número de puntos
    n = int((tf - t0) / h) + 1
    
    # Vectores de tiempo y aproximaciones
    T = np.linspace(t0, tf, n) # array de tiempo, desde t0 hasta tf, con n puntos
    X = np.zeros(n) # array para almacenar los valores de x(t) calculados mediante el método de Euler
    
    # Condición inicial
    X[0] = x0 # valor inicial x(t0)
    
    # Método de Euler
    for i in range(1, n): # iteramos i=1 hasta i=n-1 (porque i=0 es la condición inicial)
        X[i] = X[i-1] + h * f(T[i-1], X[i-1]) # en cada iteración, se calcula el siguiente valor de X utilizando la fórmula del método de Euler.
    
    return T, X # se devuelven los valores de tiempo y las aproximaciones de x(t) calculadas mediante el método de Euler.

# Definición de la función f(t, x) = dx/dt
def f(t, x):
    return -2 * x + t # la función f(t, x) que describe la derivada x_puntos = -2x + t

# Parámetros de entrada
t0 = 0.0    # tiempo inicial
tf = 2.0    # tiempo final
x0 = 1.0    # valor inicial x(t0)
h = 0.1     # incremento de tiempo

# Llamada al método de Euler
T, X = metodo_euler(f, t0, tf, x0, h)

# Mostrar los resultados
print("Tiempos:", T)
print("Aproximaciones:", X)

# Graficar los resultados
plt.plot(T, X, label='Aproximación de Euler')
plt.xlabel('Tiempo')
plt.ylabel('x(t)')
plt.title('Método de Euler')
plt.legend()
plt.grid(True)
plt.show()