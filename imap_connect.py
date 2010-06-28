#!/usr/bin/env python
import imaplib
from pprint import pprint
import os

def open_connection(verbose=False):
    #connect to the server
    hostname = 'imap.gmail.com'
    if verbose: print 'Connecting to', hostname
    connection = imaplib.IMAP4_SSL(hostname)
    
    #login to our account
    #removed username and password for security reasons
    username = ''
    password = ''
    if verbose: print 'Logging in as', username
    connection.login(username,password)
    return connection

if __name__ == '__main__':
    c = open_connection(verbose=True)
    try:
        typ, data = c.list()
        print 'Response code:', typ
        print 'Response:'
        pprint(data)
    finally:
        c.logout