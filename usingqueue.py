#-------------------------------------------------------------------------------
# Name:        usingqueue
# Purpose:
#
# Author:      Administrator
#
# Created:     29/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from multiprocessing import Process,Queue
import os,time,random

def write(q):
    for value in['A','B','C']:
        print 'Put %s to queue...'% value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.'% value

if __name__=='main__':
    print 'run start...'
    q = Queue()
    pw = Process(target=write,args=q)
    pr = Process(target=read,args=q)
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    print 'run end...'