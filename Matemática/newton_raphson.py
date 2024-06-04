# El siguiente código muestra cómo se puede implementar el método de Newton-Raphson en Python.
# Hay que definir la función y su derivada, el punto inicial p0, la tolerancia y el número máximo de iteraciones.

def funcion(x):
    return x**2 - x - 3

def derivada(x):
    return 2*x - 1

def newton_raphson(funcion, derivada, p0, tol, max_iter):
    p = p0
    for i in range(max_iter):
        p = p - funcion(p) / derivada(p)
        if abs(funcion(p)) < tol:
            break
    return p, funcion(p), abs(funcion(p))

p0 = 1.6
tol = 0.0001
max_iter = 100

p, fp, error = newton_raphson(funcion, derivada, p0, tol, max_iter)
# el error es el valor absoluto de f(p), y representa la distancia entre f(p) y 0

print("La raíz de la función es {:.2f}, f(p) = {:.2f} y el error es {:.2f}".format(p, fp, error))