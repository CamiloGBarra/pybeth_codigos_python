# El siguiente código es un juego de doble o nada en el que el usuario debe apostar una cantidad 
# de dinero a cara o cruz. 
# Si la moneda cae en cara, el usuario gana el doble de lo apostado, si cae en cruz, pierde todo.

import random

apuesta = float(input("Ingrese la cantidad a apostar:"))
moneda = random.choice(["cara", "cruz"])

# añadir el signo $ a la cantidad apostada
if moneda == "cara":
    print(f"Salió {moneda}. Felicitaciones! Ganaste $ {2*apuesta}")
else:
    print(f"Salió {moneda}. Perdiste todo")