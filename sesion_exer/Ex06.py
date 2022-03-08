# Declara 2 variables numéricas (con el valor que desees), he indica cual es mayor de los dos Si son iguales indicarlo también
# Cambia los valores iniciales para comprobar que funciona correctamente


def compara(v1, v2):
    if v1 == v2:
        print("los valores son iguales", v1)
    else:
        print("El valor máximo entre", v1, "y", v2, "es", max(v1, v2))

A = 5
B = 70

compara(A, B)

A = 45
B = 10

compara(A, B)