# -*- coding: utf-8 -*-
"""Ejercicio1_Tarea3_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i99gZdN3sfzeG0oMi85N8M_2Q1l2piXr
"""

import numpy as np

def eliminacion_gaussiana(matriz, vector):
    matriz = matriz.copy()  # Crear copia para evitar modificar la original
    vector = vector.copy()  # Copia del vector independiente
    n = len(vector)  # Número de ecuaciones

    for i in range(n):
        # Selección de pivote (pivoteo parcial)
        fila_max = i + np.argmax(np.abs(matriz[i:, i]))
        if fila_max != i:
            matriz[[i, fila_max], :] = matriz[[fila_max, i], :].copy()  # Intercambio de filas
            vector[[i, fila_max]] = vector[[fila_max, i]].copy()

        # Eliminación progresiva
        for j in range(i + 1, n):
            factor = matriz[j, i] / matriz[i, i]
            matriz[j, i:] -= factor * matriz[i, i:]
            vector[j] -= factor * vector[i]

    # Sustitución regresiva para encontrar la solución
    solucion = np.zeros(n)
    for i in range(n - 1, -1, -1):
        solucion[i] = (vector[i] - np.dot(matriz[i, i + 1:], solucion[i + 1:])) / matriz[i, i]

    return solucion

# Definir una matriz de coeficientes 4x4 y un vector de términos independientes
matriz_coef = np.array([
    [3, 2, -1, 4],
    [5, -3, 2, -1],
    [-1, 4, -2, 3],
    [2, -1, 3, 5]
], dtype=float)

vector_indep = np.array([10, 5, -3, 8], dtype=float)

# Resolver el sistema de ecuaciones
solucion = eliminacion_gaussiana(matriz_coef, vector_indep)

# Mostrar la solución
print("Solución del sistema:")
print(solucion)