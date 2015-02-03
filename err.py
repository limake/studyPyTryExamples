#-------------------------------------------------------------------------------
# Name:        err
# Purpose:
#
# Author:      Administrator
#
# Created:     26/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#--------------------------------------------------------------

#import logging

#def foo(s):
    a=1
    b=2
    c=3
#   d=a+b*c
#    print d

    return 10 /int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')

    except StandardError, e:
        logging.exception(e)

main()
print 'END'

