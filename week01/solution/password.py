"""
This module checks if a password is correct or not.
"""


def set_password():
    """This function sets a password."""
    password = input("Passwort festlegen: ")

    if len(password) < 8:
        print("Dein Passwort muss mindestens 8 Zeichen lang sein!")
        return False
    
    for zeichen in password:
        if zeichen.isdigit():
            print("Passwort erfolgreich festgelegt.")
            return True
        print("Dein Passwort muss mindestens eine Zahl enthalten!")
        return False

def check_password(password):
    """This function checks if a password is correct or not."""
    if input("Passwort: ") == password:
        print("Passwort ist richtig.")
        return True
    else:
        print("Passwort ist falsch")
        return False
    

if __name__ == "__main__":
    password = set_password()
    if password:
        check_password(password)

