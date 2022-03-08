# Lee un número por teclado que pida el precio de un producto (puede tener decimales) y calcule el precio final con IVA El
# valor del IVA será una constante que será del 21
IVA = 0.21

def Calprec(R):
    W = R * IVA
    T = R + W

R = float(input("Precio del producto: "))