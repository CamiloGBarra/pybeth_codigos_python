"""
Programa para encontrar la raíz de una función f utilizando el método de la bisección. 
Los datos de entrada son:
* la función f,
* el intervalo inicial [a,b] y
* la tolerancia TOL.

El programa retorna:
* el valor final c de la aproximación a la raíz,
* el valor f(c) y
* el error correspondiente.
"""

def f(x):
    return x**2 - 2 # la función es x^2 - 2

def biseccion(f, a, b, tol): # los argumentos son la función f, el intervalo [a,b] y la tolerancia TOL
    if f(a) * f(b) >= 0:
        raise ValueError("El método de bisección no puede aplicarse. f(a) y f(b) deben ser de signos opuestos.")
    
    c = (a + b) / 2 # se calcula el punto medio del intervalo
    for i in range(100): # se itera 100 veces
        if abs(f(c)) < tol: # si el valor absoluto de f(c) es menor que la tolerancia
            break # se sale del ciclo
        elif f(a) * f(c) < 0: # si el producto de f(a) y f(c) es menor que 0
            b = c # entonces b toma el valor de c
            """
            Si f(a) * f(c) < 0 entonces f(a) y f(c) tienen signos opuestos, lo que significa que la raíz 
            de la función se encuentra en el intervalo [a,c]. Por lo tanto, se actualiza el intervalo [a,b]
            y se calcula nuevamente el punto medio. En otras palabras, se actualiza b a c. Esto reduce el 
            intervalo a [a,c] y se repite el proceso.
            """
        else:
            a = c # a toma el valor de c, porque el producto de f(a) y f(c) es mayor que 0
            """
            Si f(a) * f(c) > 0 entonces f(a) y f(c) tienen el mismo signo, lo que significa que la raíz
            de la función se encuentra en el intervalo [c,b]. Por lo tanto, se actualiza el intervalo [a,b]
            y se calcula nuevamente el punto medio. En otras palabras, se actualiza a a c. Esto reduce el
            intervalo a [c,b] y se repite el proceso.
            """
        c = (a + b) / 2 # se calcula nuevamente el punto medio
    return c, f(c), abs(f(c)) # se retorna c, f(c) y el valor absoluto de f(c)

c, fc, error = biseccion(f, 1, 2, 1e-6)
print(f"La raíz de la función es {c}, f(c) = {fc} y el error es {error}")