users = {'hiren':'active','tarang':'inactive','guru':'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        print('inactive user is',user)
        del users[user]
        print(user,status)

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(user,status)

