'''
Created on 2013-6-15

@author: sunlzx
'''

from com.lzx.module import m1
from com.lzx.classes.obj import User
from com.lzx.classes.obj import MetricData

if __name__ == '__main__':
    pass


def fib(n):
    a, b = 0, 1
    ret = []
    while (b < n):
        ret.append(b)
        a, b = b, a + b
    return ret

fib(100);
fib2 = fib(100)
print "=========="
print fib2

print m1.add(1, 2)

user = User("sunlzx");
print user.getname()
#user.age = 0

user2 = User("lzx");
#user2.age = 1;

print "=========="
print user.age
print user2.age
print User.age

User.age = 1
print "=========="
print user.age
print user2.age
print User.age

md = MetricData()
md.show()
#print dir(MetricData)
#print dir(md)
#print dir(User)
#print dir(user2)
