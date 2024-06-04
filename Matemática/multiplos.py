# el siguiente determina si un número que se solicita al usuario es múltiplo de 2, de 5, de ambos o de ninguno.
# Se pueden modificar los valores de las variables numero1 y numero2 para determinar si el número ingresado es múltiplo de otros números.

numero1 = 2
numero2 = 5

def multiplo(a):
    if a % numero1 == 0 and a % numero2 == 0:
        return "El número {} es múltiplo de 2 y de 5".format(a)
    elif a % numero1 == 0:
        return "El número {} es múltiplo de 2, pero no de 5".format(a)
    elif a % numero2 == 0:
        return "El número {} es múltiplo de 5, pero no de 2".format(a)
    else:
        return "El número {} no es múltiplo de 2 ni de 5".format(a)
    
a = int(input("Ingrese un número entero:"))

#  % devuelve el resto de la división

print(multiplo(a))