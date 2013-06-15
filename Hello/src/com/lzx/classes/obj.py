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
    
class MetricData():
    
    def __init__(self):
        self.sum = 0
        self.max = 0
        self.min = 0
        self.avg = 0
        self.sampleCount = 0
        self.timestamp = 0        
        pass
    
    def show(self):
        print "sum:%d, max:%d, min%d, avg:%d, sampleCount:%d" \
            %(self.sum, self.max, self.min, self.avg, self.sampleCount)
    
        