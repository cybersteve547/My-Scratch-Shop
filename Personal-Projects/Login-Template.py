import scratchattach as scratch3
import os

def signin():
    # Gets username and password
    username = str(input("Username: "))
    password = str(input("Password: "))
    clear()

    # Attempts to sign in
    print("Logging in to scratch...")
    try:
        result = scratch3.login(username, password)
    except:
        # Repeats if username or password is incorrect
        input("Unable to log in.")
        clear()
        return signin()
    else:
        # Returns the session
        return result

# Creates the clear() function
clear = lambda: os.system("cls")
clear()

# Signs in
session = signin()
input("Logged in!")
clear()