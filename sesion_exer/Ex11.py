# Lee un número por teclado que pida el precio de un producto (puede tener decimales) y calcule el precio final con IVA El
# valor del IVA será una constante que será del 21
IVA = 0.21

def Calprec(R, div):
    W = R * IVA
    T = R + W
    print("Precio neto sin IVA = ", R, div)
    print("el 21% de IVA = ", W, div)
    print("Precio total del producto", T, div)


R = float(input("Precio del producto: "))
div = str(input("Indique la moneda:"))

Calprec(R, div)
