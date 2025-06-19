
import scratchattach as sa
import os

def signin():
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
        input("Unable to log in.")
        clear()
        return signin()
    else:
        # Returns the session
        return result

# Clears the screen
clear = lambda: os.system("clear")
