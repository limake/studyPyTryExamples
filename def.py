import functools

def log(text='OK'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print 'call %s %s():' % (text, func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log()
def now():
    print '2013-12-25'


def int2(x,base=2):
    return int(x,base)


kw={base:2}
int('10010',**kw)
max2=functools.partial(max,10)
