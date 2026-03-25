"""
Dieses Modul gibt n Zahlen aus.
"""


def zahlenausgeben(n):
    """Diese Funktion gibt n Zahlen aus."""
    for i in range(1, n + 1):
        print(i)

if __name__ == "__main__":
    zahlenausgeben(20)
