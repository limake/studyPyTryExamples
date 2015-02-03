def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('ban operand type')
    if x>= 0:
        return x
    else:
        return -x
def nop():
    pass


import math


def move(x, y, step, angle=0):
    nx =x + step * math.cos(angle)
    ny =y - step * math.sin(angle)
    return nx, ny

def power(x):
    return x * x


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender, age=6, city='beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

def add_end(L=[]):
    L.append('END')
    return L

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def fact(n):
    return fact_iter(1, 1, n)

def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)
    
