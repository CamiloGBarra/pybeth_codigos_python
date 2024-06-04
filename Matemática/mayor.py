# en pantalla se solicitará dos números, luego se compararán y se mostrará el mayor de ellos

def mayor(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "Los números son iguales"
    
a = float(input("Ingrese un número: "))
b = float(input("Ingrese otro número: "))

if a != b:
    print("El mayor número entre {} y {} es: {}".format(a, b, mayor(a, b)))
elif a == b:
    print("Los números {} y {} son iguales".format(a, b))

# format es una función que permite formatear strings, 
# en este caso se utilizó para reemplazar los {} por los 
# valores de las variables a, b y mayor(a, b)