# -*- coding:utf-8 -*-
'''
Created on 2013-6-15

@author: sunlzx
'''

class Animal(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.age = 0
        
        
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self) #调用父类构造方法
        pass
    
        
        
dog = Dog()
print dog.age
print dir(dog)

        