"""
Dieses Modul speichert und rechnet mit 2 Zahlen.
"""


def rechner():
    """Diese Funktion rechnet mit 2 Zahlen und gibt die Ergebnisse aus."""
    zahl1 = 10
    zahl2 = 5

    summe = zahl1 + zahl2
    differenz = zahl1 - zahl2
    differenz2 = zahl2 - zahl1
    produkt = zahl1 * zahl2
    quotient = zahl1 / zahl2
    quotient2 = zahl2 / zahl1

    print("Zahl 1:", zahl1)
    print("Zahl 2:", zahl2)
    print("Summe:", summe)
    print("Differenz:", differenz)
    print("Differenz 2:", differenz2)
    print("Produkt:", produkt)
    print("Quotient:", quotient)
    print("Quotient 2:", quotient2)

if __name__ == "__main__":
    rechner()

