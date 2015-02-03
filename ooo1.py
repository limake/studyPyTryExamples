#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     24/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass
class Dog(Mammal):
    pass
#class Bat(Mammal):
#    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
class Runnable(object):
    def run(self):
        print('Running')
class Flyable(object):
    def Fly(self):
        print('Flying')
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass

