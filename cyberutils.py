
import scratchattach as sa
import os

# Use this like so: session = cyberutils.login()
def login():
    # Gets username and password
    username = str(input("Username: "))
    password = str(input("Password: "))
    clear()

    # Attempts to sign in
    print("Logging in to scratch...")
    try:
        result = sa.login(username, password)
    except:
        # Repeats if username or password is incorrect
        input("Unable to log in. ")
        clear()
        return signin()
    else:
        # Returns the session
        input("logged in! ")
        clear()
        return result

# Clears the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")
