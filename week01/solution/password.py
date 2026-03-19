"""
This module checks if a password is correct or not.
"""


def password_checker():
    """This function checks if a password is correct or not."""
    password = "Hallo123!"
    if input("Passwort: ") == password:
        print("Password is correct.")
        return True
    else:
        print("Password is incorrect.")
        return False

if __name__ == "__main__":
    password_checker()