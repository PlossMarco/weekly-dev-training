"""
Dieses Modul zeigt mir welche Zahl die größte, kleinste und was der Durchschnitt
aus einer Liste an Zahlen ist.
"""


def groesser_zehn(zahlen):
    """Diese Funktion gibt alle Zahlen aus einer Liste die groesser als 10 sind."""
    for zahl in zahlen:
        if zahl > 10:
            print(zahl)

if __name__ == "__main__":
    groesser_zehn([4, 12, 7, 19, 3, 25])

