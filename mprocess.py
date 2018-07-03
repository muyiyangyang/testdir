# coding: utf-8
import os
from multiprocessing import Process


print "process (%s) start..." % os.getpid()
pid= os.fork()
if pid == 0:
    print 'i am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'i (%s) just created a child process (%s).' % (os.getpid(), pid)

# os.getpid()获取当前进程id     os.getppid()获取父进程id

# 子进程要执行的代码
def run_proc(name):
    print 'run child process %s (%s).' % (name, os.getpid())

if __name__ == '__main__':
    print 'parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'process will start.'
    p.start()
    p.join()
    print 'process end.'
