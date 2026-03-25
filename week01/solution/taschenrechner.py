"""
2 Zahlen und der Operator werden von der Kommandozeile eingelesen und das Ergebnis wird ausgegeben.
"""


def zahl1():
    """Diese Funktion legt die erste Zahl fest."""
    try:
        return float(input("Zahl 1: "))
    except ValueError:
        print("Bitte eine gültige Zahl eingeben!")
        return zahl1()

def zahl2():
    """Diese Funktion legt die zweite Zahl fest."""
    try:
        return float(input("Zahl 2: "))
    except ValueError:
        print("Bitte eine gültige Zahl eingeben!")
        return zahl2()

def operator():
    """Diese Funktion legt den Operator fest."""
    op = input("Operator (+, -, *, /): ")
    if op in ['+', '-', '*', '/']:
        return op
    else:
        print("Ungültiger Operator! Bitte einen der folgenden Operatoren eingeben: +, -, *, /")
        return operator()

def berechnung(a, b, op):
    """Diese Funktion berechnet das Ergebnis basierend
    auf den eingegebenen Zahlen und dem Operator."""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            print("Fehler: Division durch Null ist nicht erlaubt!")
            return None

if __name__ == "__main__":
    num1 = zahl1()
    num2 = zahl2()
    result = berechnung(num1, num2, operator)

    if result is not None:
        print("Ergebnis:", result)
