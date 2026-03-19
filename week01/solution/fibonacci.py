"""
Dieses Modul enthält eine Implementierung der Fibonacci-Folge.

Die Funktion fibonacci(n) berechnet die ersten n Werte der Fibonacci-Sequenz.
"""


def fibonacci(n):
    """Diese Funktion berechnet die ersten n Werte der Fibonacci-Sequenz."""
    a = 0
    b = 1

    for _ in range(n):
        print(a)
        a, b = b, a + b
        # neues a = altes b
        # neues b = altes a + altes b


fibonacci(10)

if __name__ == "__main__":
    fibonacci(10)
