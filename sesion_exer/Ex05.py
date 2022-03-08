'''
Realiza un programa que declare cuatro variables enteras A, B, C y D y asígnale un valor a cada una. A continuación realiza l as
instrucciones necesarias para que:
•
B tome el valor de C
•
C tome el valor de A
•
A tome el valor de D
•
D tome el valor de B
'''

A = 5
B = 'Victoria'
C = 2.6
D = 'Alejandra'

print('Valor de A =', A)
print('Valor de B =', B)
print('Valor de C =', C)
print('Valor de D =', D)

B2 = B
B = C
print('B toma el valor de C, B = ', B)
C = A
print('C toma el valor de A, C = ', C)
A = D
print('A toma el valor de D, A = ', A)
D = B2
print('D toma el primer valor de B, D = ', D)
D = B
print('D toma el valor actual de B, D = ', D)