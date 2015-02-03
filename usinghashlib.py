#-------------------------------------------------------------------------
# Name:        usinghashlib

# Purpose:
#
# Author:      Administrator
#
# Created:     30/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------

import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

md5 = hashlib.md5()
md5.update('how to use md5 in')
md5.update('python hashlib?')
print md5.hexdigest()


import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in')
sha1.update('python hashlib?')
print sha1.hexdigest()
