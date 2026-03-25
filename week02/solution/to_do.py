"""
Dieses Modul implementiert eine To-Do-Liste, die es dem Benutzer ermöglicht
Aufgaben hinzuzufügen, anzuzeigen und zu entfernen.
"""


def new_task():
    """Diese Funktion ermöglicht es dem Benutzer, eine neue Aufgabe hinzuzufügen."""
    with open("task.txt", "a", encoding="utf-8") as f:
        hinzufügenf.write(input("Aufgabe: ") + "\n")

def show_tasks():
    """Diese Funktion zeigt alle Aufgaben in der To-Do-Liste an."""
    try:
        with open("task.txt", "r", encoding="utf-8") as f:
            aufgaben = f.read().splitlines()
            for nummer, aufgabe in enumerate(aufgaben, start=1):
                print(nummer, aufgabe)
    except FileNotFoundError:
        print("Keine Aufgaben vorhanden.")

def remove_task():
    """Diese Funktion ermöglicht es dem Benutzer, eine Aufgabe zu entfernen."""
    try:
        with open("task.txt", "r", encoding="utf-8") as f:
            aufgaben = f.read().splitlines()
            nummer = int(input("Welche Aufgabe löschen? "))
            aufgaben.pop(nummer - 1)
            with open("task.txt", "w", encoding="utf-8") as f:
                for aufgabe in aufgaben:
                    f.write(aufgabe + "\n")
            print("Aufgabe", nummer, "gelöscht.")
    except (IndexError, ValueError):
        print("Ungültige Eingabe. Bitte gib eine gültige Aufgabennummer ein.")
        return remove_task()

if __name__ == "__main__":
    while True:
        show_tasks()
        auswahl = input("Was möchtest du tun? (hinzufügen/entfernen/beenden): ")
        if auswahl == "hinzufügen":
            new_task()
        elif auswahl == "entfernen":
            remove_task()
        elif auswahl == "beenden":
            break
        else:
            print("Ungültige Eingabe.")