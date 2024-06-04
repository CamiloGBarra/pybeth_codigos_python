# se solicitará en pantalla un número real y un número entero, 
# luego se mostrará el número real elevado a la potencia del número entero ingresado.

def potencia(x, n):
    return x**n

x = float(input("Ingrese un número real: "))
n = int(input("Ingrese un número entero: "))
print("El número {} elevado a la potencia {} es: {}".format(x, n, potencia(x, n)))

print("Las primeras 5 potencias de {} son:".format(x))

for i in range(1, 6):
    print(potencia(x, i))