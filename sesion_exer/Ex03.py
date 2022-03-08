# Escribe un programa que realice lo siguiente declarar dos variables X e Y de tipo int dos variables N y M de tipo float y
# asigna a cada una un valor

def suma(A, B, C, D):
    W = A + B + C + D
    return W

def resta(A, B):
    W = A - B
    return W

def multi(A, B, C, D):
    W = A * B * C * D
    return W

def divi(A, B):
    W = A / B
    return W

def resto(A, B):
    W = A % B
    return W

def dob(A):
    W = A * 2
    return W

X = 34
Y = 45
N = 2.5
M = 8.1

print("X vale", X)
print("Y vale", Y)
print("N vale", N)
print("M vale", M)

print("La suma de X =", X, "mas Y =", Y, "da como resultado:", suma(X, Y, 0, 0))
print("La resta de X =", X, "menos Y =", Y, "da como resultado:", resta(X, Y))
print("La multiplicación de X =", X, "por Y =", Y, "da como resultado:", multi(X, Y, 0, 0))
print("La división de X =", X, "entre Y =", Y, "da como resultado:", divi(X, Y))
print("el resto de la división de X =", X, "entre Y =", Y, "da como resultado:", resto(X, Y))
print("La suma de N =", N, "mas M =", M, "da como resultado:", suma(N, M, 0, 0))
print("La resta de N =", N, "menos M =", M, "da como resultado:", resta(N, M))
print("La multiplicación de N =", N, "por M =", M, "da como resultado:", multi(N, M, 0, 0))
print("La división de N =", N, "entre M =", M, "da como resultado:", divi(N, M))
print("el resto de la división de N =", N, "entre M =", M, "da como resultado:", resto(N, M))
print("La suma de X =", X, "mas N =", N, "da como resultado:", suma(X, N, 0, 0))
print("La división de Y =", Y, "entre M =", M, "da como resultado:", divi(Y, M))
print("el resto de la división de Y =", Y, "entre M =", M, "da como resultado:", resto(Y, M))
print("El doble de la variable X =", X, "es:", dob(X))
print("El doble de la variable Y =", Y, "es:", dob(Y))
print("El doble de la variable N =", N, "es:", dob(N))
print("El doble de la variable M =", M, "es:", dob(M))
print("La suma de las variables X =", X, "mas N =", N, "mas Y =", Y, "mas M =", M, "da como resultado", suma(X, N, Y, M))
print("El producto de las variables X =", X, "mas N =", N, "mas Y =", Y, "mas M =", M, "da como resultado", multi(X, N, Y, M))





