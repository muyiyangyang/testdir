from functools import wraps

def logprint(level='info'):
    def logwrap(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if level == 'error':
                print 111111111111
            print 2222222222222222
            return func(*args, **kwargs)
        return wrapper
    return logwrap

@logprint('error')
def f():
    print 3333333333333
