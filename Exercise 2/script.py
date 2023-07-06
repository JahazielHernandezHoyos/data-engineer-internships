import numpy as np


def generar_serie():
    """
    Genera una serie de números de acuerdo a las siguientes condiciones:
    - Cada 100 números, el número generado es un múltiplo de los primeros números naturales.
    - La serie termina cuando se alcanza el número 5000.
    """
    numeros = np.arange(
        1, 5001, 2
    )  # Genera un arreglo con los números impares del 1 al 5000
    indices = np.arange(
        100, 5001, 100
    )  # Genera un arreglo con los índices donde se deben modificar los números
    numeros[indices - 1] += np.arange(
        1, 51
    )  # Incrementa los números en función de los múltiplos de los primeros números naturales
    return numeros


serie = generar_serie()
for numero in serie:
    print(numero)
