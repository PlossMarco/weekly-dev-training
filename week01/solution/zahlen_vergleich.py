"""
Dieses Modul überprüft ob eine Zahl poitiv, negativ oder 0 ist.
"""


def zahlenvergleich(zahl):
    """Diese Funktion überprüft ob eine Zahl poitiv, negativ oder 0 ist."""
    if zahl > 0:
        print("Die Zahl ist positiv.")
    elif zahl < 0:
        print("Die Zahl ist negativ.")
    else:
        print("Die Zahl ist 0.")


if __name__ == "__main__":
    zahlenvergleich(10)
    zahlenvergleich(-5)
    zahlenvergleich(0)
