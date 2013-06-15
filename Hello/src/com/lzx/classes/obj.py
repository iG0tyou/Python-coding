'''
Created on 2013-6-15

@author: sunlzx
'''

class User(object):
    '''
    classdocs
    '''
    age = 10;

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        
    def setname(self, name):
        self.name = name;
    
    def getname(self):
        return self.name
        