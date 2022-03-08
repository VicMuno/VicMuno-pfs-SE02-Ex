# Realiza una aplicación que nos pida un número de ventas a introducir, después nos pedirá tantas ventas por teclado como
# número de ventas se hayan indicado Al final mostrara la suma de todas las ventas Piensa que es lo que se repite y lo que no



def ventas(A):
    C = 0
    while A > 0 :
        B = int(input("Venta:"))
        C = C + B
        print(C)
        A -= 1


A = int(input("Introduce las ventas del día:"))
print(ventas(A))
