import scratchattach as sa

# Initialize variables
user = sa.get_user("griffpatch") # Change this if you want to look at a different users followers
allfollowers = []
offset = 0

# Start the main loop
while True:
    # Get a list of followers
    for follower in user.followers(limit=40, offset=offset):
        # Initialize more variables
        followercount = follower.follower_count()
        username = follower.username
        # Sorts the followers
        i = 0
        reali = 0
        while reali < len(allfollowers):
            if followercount < allfollowers[i][0]:
                i += 1
            reali += 1
        # Checks if the list already contains that follower
        i2 = 0
        insert = True
        while i2 < len(allfollowers):
            if allfollowers[i2][1] == username:
                insert = False
            i2 += 1
        # Inserts the follower into the list
        if insert:
            allfollowers.insert(i, [followercount, username])
        
        # What you want to do with the followers
        print(len(allfollowers))
        print(allfollowers)
        print("\n")

    offset += 40
