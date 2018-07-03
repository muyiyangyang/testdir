# coding: utf-8
from multiprocessing import Pool
import os
import time
import random

def long_time_task(name):
    print 'run task %s (%s) ...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    print 'parent process %s.' % os.getpid()
    #p = Pool(4)
    p = Pool() #默认是cpu核数，即最多同时可以执行的进程数，可设置大于等于小于CPU核数
    for i in range(16):
        p.apply_async(long_time_task, args=(i,))
    print 'waiting for all subprocesses done.'
    p.close()
    p.join()
    print 'all subprocesses done.'
