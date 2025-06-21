import scratchattach as sa
import cyberutils as cu

print("please log in for safety measures.")
session = cu.login()
print("who should i get data on?")
name = input("")
limits = [10, 5, 5]
max_depth = 3
visited = []
cu.clear()

def maketree(username, lvl):
    tree = []
    if lvl > 0:
        indent = ("│" * (lvl - 1)) + "├"
    else:
        indent = ""
    try:
        user = session.connect_user(username)
        if username in visited:
            print(indent + username + " (already seen)")
        else:
            visited.append(username)
            print(indent + username)
            if lvl < max_depth and lvl < len(limits):
                for follower in user.following(limit=limits[lvl]):
                    tree.append(follower.username)
    except Exception as e:
        print(indent + username + " (broken user) error: " + str(e))
    with open(username + ".txt", "w") as file:
        file.write(username + " is following\n")
        for i in tree:
            file.write(i + "\n")

maketree(name, 0)