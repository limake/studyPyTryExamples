#-------------------------------------------------------------------------------
# Name:        usingmultprocessing

# Purpose:
#
# Author:      Administrator
#
# Created:     29/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>p
#-------------------------------------------------------------------------------

from multiprocessing import Process
import os

def run_proc(name):
    print '********************'
    print name
    #print os.getpid()
    #print 'Run child prorrcess %s(%s)...'%(name,os.getpid())
    print '********************'

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process( target=run_proc,args='test')
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
