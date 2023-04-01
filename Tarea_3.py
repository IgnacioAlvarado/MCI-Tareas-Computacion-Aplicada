#Tarea 3

import numpy as np

#sistema de ecuaciones del problema:

#1x + 3y = 300
#1.5x + 2y = 350

#Plantear matriz:

A = np.array ([[1.0, 3.0], [1.5, 2.0]])

#solución de cada ecuación
B = np.array ([300, 350])

print("Matrix del problema:", A,B)

#resolver para X junto con Y y comprobar después con regla de crammer

x, y = np.linalg.solve(A, B)
print("Solución del sistema de ecuaciones utilizando la función linalg:", x, y)

#Ahora resolver con regla de cramer:

#Plantear determinante:
d = ((A[0][0] * A[1][1])-((A[0][1] * A[1][0])))

#Para X:
x1 = ((B[0]* A[1][1])-(B[1] * A[0][1]))

#Para Y:
y1 = ((B[1]* A[0][0])-(B[0] *A[1][0]))
x = x1/d
y = y1/d

#resultados de crammer

print("Resultado de x utilizando Regla de Cramer:", x)
print("Resultado de y utilizando Regla de Cramer:", y)
