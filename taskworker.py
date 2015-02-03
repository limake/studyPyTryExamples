#-------------------------------------------------------------------------------
# Name:        taskworker.py
# Purpose:
#
# Author:      Administrator
#
# Created:     29/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time,sys,Queue
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
server_addr = '127.0.0.1'
print('Connect to server %s...'%server_addr)
m = QueueManager(address=(server_addr,5000),authkey='abc')
m.connect()
task = m.get_task_queue()
result =m.get_result_queue()
for i in range(10):
    try:
        n=taask.get(timeout=1)
        print('run task %d * %d...'%(n,n))
        r='%d*%d=%d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except QueueEmpty:
        print('task queue is empty.')
print('worker exit.')