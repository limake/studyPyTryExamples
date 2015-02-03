#-------------------------------------------------------------------------------
# Name:        mydict
# Purpose:
#
# Author:      Administrator
#
# Created:     26/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Dict(dict):
     def __init__(self,**kw):
        super(Dict,self).__init__(**kw)

     def __getatter__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

     def __setatter__(self,key,value):
        self[key] = value