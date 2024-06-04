# sirve para obtener el valor de π utilizando la fórmula de Wallis. 
# Se obtiene un gráfico.

def calcular_pi(n):
    pi = 1 # se empieza en 1 para evitar multiplicar por 0
    for i in range(1, n+1): # acá se empieza en 1 para evitar dividir por 0
        pi *= (2*i) / (2*i - 1) * (2*i) / (2*i + 1)
    return pi

n = int(input("Ingrese la cantidad de términos a utilizar para calcular π: "))

print("El valor aproximado de π con {} términos es: {}".format(n, 2*calcular_pi(n)))

# graficar cómo se acerca el valor de pi a medida que se aumenta la cantidad de términos
import matplotlib.pyplot as plt

n = 50
pi = [2*calcular_pi(i) for i in range(1, n+1)]
plt.plot(range(1, n+1), pi)
plt.xlabel("Cantidad de términos")
plt.ylabel("Valor de π")
plt.title("Aproximación de π")
plt.show()