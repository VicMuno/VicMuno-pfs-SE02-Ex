# Haz una aplicación que calcule el área de un circulo (pi*R 2 El valor del radio se pedirá por teclado (recuerda pasar de str a
# float Usa la constante PI y el método pow

import math
PI = math.pi

def area(R):
    W = (PI*(math.pow(R, 2)))
    return W

R = str(input("Introduce radio de la circunferencia: "))

print("El area de un círculo con un radio de", R, "es igual a:", area(float(R)))