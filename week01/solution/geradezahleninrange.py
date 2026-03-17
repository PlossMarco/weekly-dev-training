"""
Dieses Modul gibt alle geraden Zhalen in einem bestimmten Bereich aus.
"""


def gerade_zahlen_in_range(n):
    """Diese Funktion gibt alle geraden Zhalen in einem bestimmten Bereich aus."""
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    gerade_zahlen_in_range(20)