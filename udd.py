import scratchattach as sa
import cyberutils as cu
import math

print("please log in for safety measures.")
session = cu.login()
print("who should i get data on?")
name = input("")
max_depth = 3
cu.clear()

def maketree(username, lvl):
    tree = []
    try:
        user = session.connect_user(username)
        print(username)
        count = math.ceil(user.follower_count() / 50)
        print(user.follower_count())
        for i in range(count):
            for follower in user.followers(limit=50, offset=i * 50):
                tree.append(follower.username)
                print(follower.username)
    except Exception as e:
        print(username + " (broken user) error: " + str(e))
    print(len(tree))
    tree = list(set(tree))
    print(len(tree))
    with open(username + ".txt", "w") as file:
        file.write(username + "'s followers are\n")
        for i in tree:
            file.write(i + "\n")

maketree(name, 0)