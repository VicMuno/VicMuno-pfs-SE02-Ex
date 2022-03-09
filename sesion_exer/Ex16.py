# Crea una aplicación que nos pida un día de la semana y que nos diga si es un día laboral o no Se recomienda el uso de if

TupLab = ("LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES")

TupNoL = ("SABADO", "DOMINGO")

def Comdia(A):
    if A in TupLab:
        print("El día", A, "es laboral.")
    elif A in TupNoL:
        print("El día", A, "no es laboral.")
    else:
        print("El día", A, "No se reconoce.")


A = str(input("Introduce un día de la semana:")).upper()

Comdia(A)