

TupSig = ("+", "-", "*", "/", "^", "%")

def calcula(Num1, Num2, Sig):
    if Sig == "+":
        Resul = Num1 + Num2
    elif Sig == "-":
        Resul = Num1 - Num2
    elif Sig == "*":
        Resul = Num1 * Num2
    elif Sig == "/":
        Resul = Num1 / Num2
    elif Sig == "^":
        Resul = Num1 ^ Num2
    else:
        Resul = Num1 % Num2

    return Resul



Num1 = int(input("Introduce el primer número:"))
Num2 = int(input("Introduce el segundo número:"))
Sig = str(input("Introduce el signo de la operación:"))

if Sig in TupSig:
    print("El resultado es:", calcula(Num1, Num2, Sig))
else:
    print("El signo introducido no es válido, por favor selecciones uno de los siguientes:", TupSig)
