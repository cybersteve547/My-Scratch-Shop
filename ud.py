import scratchattach as sa

name = "griffpatch"
limits = [10, 5]
max_depth = 2
list = []

def tree(username, lvl):
    print(username)
    list.append(lvl + username)
    try:
        user = sa.get_user(username)
        if len(lvl) < max_depth:
            for follower in user.following(limit=limits[len(lvl)]):
                tree(follower.username, lvl + " ")
    except:
        list.append(lvl + " broken user")

tree(name, "")
for i in list:
    print(i)