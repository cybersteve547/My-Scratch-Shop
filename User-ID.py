import scratchattach as sa

def UserID(User):
    return(sa.get_user(User).id)

print(UserID("cybersteve547"))
