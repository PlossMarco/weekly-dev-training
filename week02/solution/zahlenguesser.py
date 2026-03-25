"""
Dieses Modul implementiert ein einfaches Zahlenguesser-Spiel,
bei dem der Benutzer eine Zahl zwischen 1 und 100 erraten muss.
Das Spiel gibt Feedback, ob die geratene Zahl zu hoch, zu niedrig oder korrekt ist.
"""

import random

def user_guess():
    """Der User legt in dieser Funktion eine Zahl fest."""
    while True:
        try:
            return int(input("Dein guess: "))
        except ValueError:
            print("Bitte gib eine gültige Zahl (1 - 100) ein!")
            return user_guess()

def random_number():
    """Diese Funktion generiert eine zufällige Zahl zwischen 1 und 100."""
    return random.randint(1, 100)

def zahlenguesser(guess, random_number_giver):
    """Diese Funktion vergleicht die geratene Zahl mit der zufälligen Zahl und gibt Feedback."""
    if guess > random_number_giver:
        print("Zu hoch!")
    elif guess < random_number_giver:
        print("Zu niedrig!")
    else:
        print("100 Punkte für Ravenclaw!!")

if __name__ == "__main__":
    random_num = random_number()
    guess_num = user_guess()

    while guess_num != random_num:
        zahlenguesser(guess_num, random_num)
        guess_num = user_guess()
    print("Ach scheiße, woher weißt du das?! die Zahl war wirklich", random_num)
