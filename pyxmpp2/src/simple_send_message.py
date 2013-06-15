#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Example of the 'simple API' usage.

The simplest possible way to send an XMPP message.
"""

from getpass import getpass
from pyxmpp2.simple import send_message
from pyxmpp2.settings import XMPPSettings

#your_jid = raw_input("Your jid: ")
#your_password = getpass("Your password: ")
#target_jid = raw_input("Target jid: ")
#message = raw_input("Message: ")
#    
#send_message(your_jid, your_password, target_jid, message)


settings = XMPPSettings({
                            "password": "abc",
                            "starttls": True,
                            "tls_verify_peer": False,
                            "server": "192.168.1.121"
                        })
i = 0
while i < 100:
    i += 1
    print i
    send_message("abc@sunlzx-pc", "abc", "admin@sunlzx-pc", "hell0", settings=settings)
