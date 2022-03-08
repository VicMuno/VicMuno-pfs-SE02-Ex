# Muestra los números del 1 al 100 (ambos incluidos) divisibles entre 2 y 3 Utiliza el bucle que desees

A = 1

def divi(A):
    W = A % 2
    if W == 0:
        print("El número", A, "es divisible entre 2, su resto es:0 ", A / 2)
    else:
        W = A % 3
        if W == 0:
            print("El número", A, "es divisible entre 3, su resto es:0 ", A / 3)

while A <= 100:
    print(divi(A))
    A += 1