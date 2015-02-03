class student(object):

    def __init__(self,name,score):


        self.name=name
        self.score=score

    def print_score(self):
        print '%s: %s' %(self.name,self.score)

class Animal(object):
    def run(self):
        print 'Animal is running...'
        
class Dog(Animal):
    def run(self):
        print'dog is running...'

class Cat(Animal):
    def run(self):
        print 'cat is running...'

def run_twice(animal):
    animal.run()
    animal.run()


