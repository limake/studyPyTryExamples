#-------------------------------------------------------------------------------
# Name:        usingImage
# Purpose:
#
# Author:      Administrator
#
# Created:     30/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Image
im = Image.open('d:\\a.jpg')
w,h=im.size
im.thumbnail((w//2,h//2))
im.save('d:\\b.jpg','jpeg')


