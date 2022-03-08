# Lee un número por teclado e indica si es divisible entre 2 (resto 0 Si no lo es, también debemos indicarlo

def divi(R):
    W = R % 2
    if W == 0:
        print("El número", R, "es divisible entre 2, su resto es:0 ", R / 2 )
    else:
        print("El número", R, "no es divisible entre 2, su resto es:", W)

R = float(input("Introduce un número: "))
divi(R)