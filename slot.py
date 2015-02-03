#class Student(object):
#    def get_score(self):
#        return self._score
#    def set_score(self,value):
#        if not isinstance(value,int):
#            raise ValueError('score must be an integer!')
#        if value<0 or value>100:
#            raise ValueError('score must betwwen 0~100!')
#        self._score = value    
            

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
       self._birth=value

    @property
    def age(self):
        return 2014-self._birth
       
                
