#-------------------------------------------------------------------------
# Name:        usingjson
# Purpose:
#
# Author:      Administrator
#
# Created:     28/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------

import json


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
jsonStr = json.dumps(s, default=lambda obj: obj.__dict__)

print 'Student object json string : ', jsonStr


def dict2studdent(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str, object_hook=dict2studdent))
