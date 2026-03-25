"""
This module allows you to set a username and password and check their validity.
"""


def set_password():
    """This function sets a password."""
    password = input("Passwort festlegen: ")

    if len(password) < 8:
        print("Dein Passwort muss mindestens 8 Zeichen lang sein!")
        return set_password()

    for zeichen in password:
        if zeichen.isdigit():
            with open("password.txt", "w", encoding="utf-8") as f:
                f.write(password)
            print("Passwort erfolgreich festgelegt.")
            return password
    print("Dein Passwort muss mindestens eine Zahl enthalten!")
    return set_password()

def load_password():
    """This function loads the password from a file."""
    try:
        with open("password.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Es wurde noch kein Passwort festgelegt.")
        return None

def check_password(password):
    """This function checks if a password is correct or not."""
    if input("Passwort: ") == password:
        print("Passwort ist richtig.")
        return True
    else:
        print("Passwort ist falsch")
        return False

def set_username():
    """This function sets a username."""
    username = input("Benutzername festlegen: ")
    if len(username) < 3:
        print("Dein Benutzername muss mindestens 3 Zeichen lang sein!")
        return set_username()
    with open("username.txt", "w", encoding="utf-8") as f:
        f.write(username)
    print("Benutzername erfolgreich festgelegt.")
    return username

def load_username():
    """This function loads the username from a file."""
    try:
        with open("username.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Es wurde noch kein Benutzername festgelegt.")
        return None

def check_username(username):
    """This function checks if a username is correct or not"""
    if input("Benutzername: ") == username:
        print("Benutzername ist richtig.")
        return True
    else:
        print("Benutzername ist falsch")
        return False

if __name__ == "__main__":
    import os
    if os.path.exists("username.txt"):
        stored_username = load_username()
        for i in range(3):
            if check_username(stored_username):
                print("Benutzername korrekt!")
                break
        else:
            print("Zu viele Fehlversuche. Bitte versuche es später erneut.")
    else:
        stored_username = set_username()

    if os.path.exists("password.txt"):
        stored_password = load_password()
        for i in range(3):
            if check_password(stored_password):
                print("Passwort korrekt!")
                break
        else:
            print("Zu viele Fehlversuche. Bitte versuche es später erneut.")

    else:
        stored_password = set_password()
        if stored_password:
            for i in range(3):#
                if check_password(stored_password):
                    print("Passwort korrekt!")
                    break
            else:
                print("Zu viele Fehlversuche. Bitte versuche es später erneut.")
