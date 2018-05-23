import logging
from functools import wraps

def withlog(level):
    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            for arg in args:
                print arg
            if level == 'warning':
                logging.warning('%s log warning' % func.__name__)
            elif level == 'error':
                logging.error('%s log error' % func.__name__)
            return func(*args, **kwargs)
        return wrapped
    return wrapper

@withlog('warning')
def func1(a, b, c):
    print 111111

@withlog('error')
def func2():
    print 222222222222

func1(1,2,3)
func2()
