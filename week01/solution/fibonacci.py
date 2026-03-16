"""
Dieses Modul enthält eine Implementierung der Fibonacci-Folge.

Die Funktion fibonacci(n) berechnet die ersten n Werte der Fibonacci-Sequenz.
"""


def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        a, b = b, a + b
        """neues a = altes b
        neues b = altes a + altes b"""


fibonacci(10)
