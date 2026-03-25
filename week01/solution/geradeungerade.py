"""
Dieses Modul prüft ob Zahlen gerade oder ungerade sind.
"""


def gerade_ungerade(zahl):
    """Diese Funktion prüft ob Zahlen gerade oder ungerade sind."""
    if zahl % 2 == 0:
        print("Die Zahl ist gerade.")
    else:
        print("Die Zahl ist ungerade.")

if __name__ == "__main__":
    gerade_ungerade(10)
    gerade_ungerade(5)
