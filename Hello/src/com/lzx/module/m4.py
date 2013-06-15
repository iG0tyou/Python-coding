'''
Created on 2013-6-15

@author: sunlzx
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        print "testName1"
        pass
    
    def testName2(self):
        print "name2"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()