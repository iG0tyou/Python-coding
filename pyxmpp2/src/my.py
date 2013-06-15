'''
Created on 2013-6-15

@author: sunlzx
'''
import time

if __name__ == '__main__':
    pass

import logging
from pyxmpp2.jid import JID
from pyxmpp2.client import Client
logging.basicConfig(level = logging.DEBUG)
client = Client(JID("abc@sunlzx-PC"),[])
client.connect()

print "sleep..."
time.sleep(100000)