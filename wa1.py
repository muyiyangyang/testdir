import logging
from functools import wraps

def logfunc(level):
    def logw(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if level == 'error':
                logging.error('%s log error' % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return logw

@logfunc('error')
def func1(a, b):
    print 1122

func1(11, 22)
