import scratchattach as scratch3
import time
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
user = session.get_linked_user()
input("Logged in!")
clear()

# Edit as required!
MESSAGE = "This is an automated response, I will respond presonally as soon as i can."

print("Automated response server started!")
while True:
    print("Started checking for comments that need replies!")
    comments = user.comments()
    replied = 0
    for comment in comments:
        # Gets info about the comment
        commentID = comment["CommentID"]
        replies = comment["Replies"]
        commenter = comment["User"]
        content = comment["Content"]
        commenterID = scratch3.get_user( commenter ).id
        # Checks if the comment or any of the replies are by the owner of the profile
        needsreply = True
        if commenter == str(session.get_linked_user()):
            needsreply = False
        else:
            for reply in replies:
                if reply["User"] == str(session.get_linked_user()):
                    needsreply = False
        # Replies if needed
        if needsreply:
            user.reply_comment( MESSAGE, parent_id=commentID, commentee_id=commenterID )
            print("Replied to " + commenter + "'s comment" + ' "' + content + '".')
            replied += 1
    print("Replied to " + str(replied) + " comments!")
    # Waits a little bit
    time.sleep(60)