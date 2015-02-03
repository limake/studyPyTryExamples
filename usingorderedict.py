#-------------------------------------------------------------------------------
# Name:        usingorderedict
# Purpose:
#
# Author:      Administrator
#
# Created:     29/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from collections import OrderedDict
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdateOrderedDict,self).__init__()
        self._capacity=capacity

    def __setitem__(self,key,value):
        containskey=1 if key in self else 0
        if len(self) - containskey >=self._capacity:
            last = self.popitem(last=False)
            print'remove:',last
        if containskey:
            del self[key]
            print'set:',(key,value)
        else:
            print'add:',(key,value)
        OrderedDict.__setitem__(self,key,value)

