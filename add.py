def add(x,y,f):
    return f(x)+f(y)


def is_odd(n):
    return n%2==1

filter(is_odd,[1,2,4,5,6,7,9,10,15])

def not_empty(s):
    return s and s.strip()

def reversed_cmp(x,y):
    if x>y:
        return-1
    if x<y:
        return 1
    return 0

def cmp_ignore_case(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum


    
    
def count():
    fs=[]
    for i in range(1,4):
        def f(j):
            def g():
             return j*j
            return g
        fs.append(f(i))
    return fs


