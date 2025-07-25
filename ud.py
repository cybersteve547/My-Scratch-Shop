import scratchattach as sa
import cyberutils as cu

print("please log in for safety measures.")
session = cu.login()
print("who should i get data on?")
name = input("")
limits = [10, 5, 5]
max_depth = 3
tree = []
visited = []
cu.clear()

def maketree(username, lvl):
    if lvl > 0:
        indent = ("│" * (lvl - 1)) + "├"
    else:
        indent = ""
    try:
        user = session.connect_user(username)
        if username in visited:
            tree.append(indent + username + " (already seen)")
            print(indent + username + " (already seen)")
        else:
            visited.append(username)
            tree.append(indent + username)
            print(indent + username)
            if lvl < max_depth and lvl < len(limits):
                for follower in user.following(limit=limits[lvl]):
                    maketree(follower.username, lvl + 1)
    except Exception as e:
        tree.append(indent + username + " (broken user)")
        print(indent + username + " (broken user) error: " + str(e))

maketree(name, 0)
with open(name + ".txt", "w") as file:
    file.write("tree of who " + name + " is following on scratch\n")
    for i in tree:
        file.write(i + "\n")