import logging
from functools import wraps

def logwrap(level):
    def wapper(func):
        @wraps(func)
        def logw(*args, **kws):
            if level == 'warning':
                print 'aaaaaaaaaaaaaaa'
                logging.warning('log waring asdfdsf %s' % func.__name__)
            return func(*args, **kws)
        return logw
    return wapper

@logwrap('warning')
def aafunc():
    print 'bbbbbbbbbbbbbbbbbbbb'

aafunc()
    
