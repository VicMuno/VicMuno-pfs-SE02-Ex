# Escribe una aplicación que valide el password esta está definida con una variable de tipo str que contenga una
# contraseña cualquiera Después se te pedirá que introduzcas la contraseña, tienes 3 intentos Si la contraseña introducida es
# correcta ya no la pedirá mas mostrando un mensaje diciendo “ Piensa bien en la condición de salida 3
# intentos y si aciertas sale, aunque le queden intentos)


Contr = 'Victoria'
A = 1
while A <= 3:
    cuse = str(input("Introduce la contraseña:"))

    if cuse == Contr:
        print("¡Felicidades has accedido!")
        break
    elif A == 3:
        print("Has llegado al número total de intentos y no has podido acceder")
        break
    else:
        A += 1
