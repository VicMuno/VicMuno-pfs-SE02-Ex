
TupSig = ("+", "-", "*", "/", "^", "%")

Num1 = int(input("Introduce el primer número:"))
Num2 = int(input("Introduce el segundo número:"))
Sig = input("Introduce el signo de la operación:")



if Sig in TupSig:
    operacion = eval(str(Num1) + str(Sig) + str(Num2))
    operacion = print("El resultado es:", operacion)
else:
    print("El signo introducido no es válido, por favor selecciones uno de los siguientes:", TupSig)
