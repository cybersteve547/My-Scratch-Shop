import scratchattach as sa
import cyberutils as cu

print("please log in for safety measures.")
session = cu.login()
print("who should i get data on?")
name = input("")
limits = [10, 5, 2, 2]
max_depth = 4
list = []
cu.clear()

def tree(username, lvl):
    print(lvl + username)
    list.append(lvl + username)
    try:
        user = session.connect_user(username)
        if len(lvl) < max_depth:
            for follower in user.following(limit=limits[len(lvl)]):
                tree(follower.username, lvl + "|")
    except:
        list.append(lvl + " broken user")

tree(name, "")
with open(name + ".txt", "w") as file:
    file.write("tree of who " + name + " is following on scratch\n")
    for i in list:
        file.write(i + "\n")