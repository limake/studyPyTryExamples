#-------------------------------------------------------------------------------
# Name:        usingpool
# Purpose:
#
# Author:      Administrator
#
# Created:     29/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from multiprocessing import Pool
import os, time ,random

def long_time_task(name):
    print 'Run task %s (%s)...'%(name,os.getpid())
    start = time.time()
    time.sleep(random.random()*7*random.random())
    end = time.time()
    print 'Task %s run %0.2f second.'%(name,(end - start))

if __name__=='__main__':
    print 'Parent process %s.'%os.getpid()
    p=Pool()
    for i in range(10):
        p.apply_async(long_time_task,args=(i,))
    print 'waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
