# El siguiente código es un juego de adivinanza en el que el usuario debe adivinar un número entre 1 y 10.

import random

numero = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Adiviná el número entre 1 y 10:"))
    intentos = intentos + 1 
    if intento == numero:
        break

print(f"¡Adivinaste! El número era {numero} y te llevó {intentos} intentos adivinarlo.")