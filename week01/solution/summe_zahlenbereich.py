"""
Dieses Modul addiert alle Zhalen in einem Bereich.
"""


def summe_zahlen_bereich(n):
    """Diese Funktion addiert alle Zhalen in einem Bereich."""
    summe = 0
    for i in range(1, n + 1):
        summe += i
    print("Die Summe der Zahlen von 1 bis", n, "ist:", summe)

if __name__ == "__main__":
    summe_zahlen_bereich(20)