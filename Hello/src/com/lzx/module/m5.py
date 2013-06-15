'''
Created on 2013-6-15

@author: sunlzx
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        print "setUP..."
        pass


    def tearDown(self):
        print "tearDown..."
        pass


    def testName(self):
        print "test"
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()