#-------------------------------------------------------------------------------
# Name:        cheatuser
# Purpose:
#
# Author:      Administrator
#
# Created:     30/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if user not in db.keys():
        return False
    import hashlib
    md5=hashlib.md5()
    md5.update(password)
    miwen=md5.hexdigest()
    if miwen==db[user]:
        return True
    else:
        return False
