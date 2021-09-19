# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:13:10 2018

@author: uzzlej

The purpose of this is to create a node that will send all information to a 
single relay node so it can be broadcast throughout the entire network. Removes
the first part of the message id before printing out the message received.
This is designed to only broadcast over a single string, one I will call 'Darwin'"""
import socket
import random
import thread
class userNode:
    def __init__(self,p,r):
        #The port this user node receives information from
        self.port = p
        #The port this user node sends information to
        self.relayPort = r
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a datagram socket (UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Make the socket reusable
        self.sock.setblocking(False) # Set socket to non-blocking mode
        self.host = '127.0.0.1'
        self.sock.bind((self.host, self.port))
    def listenThread(self):
        while True:
            try:
                message, address = self.sock.recvfrom(self.port)
                prntMsg = message
                #print "Message received."
                #prntMsg will be what we print
                msgID = prntMsg[:7]
                prntMsg = prntMsg[7:]
                if message:
                    print "Message from port:"+str(self.relayPort)+" printed by port "+str(self.port)+": "+prntMsg
            except:
                pass

    def listen(self):
        """Pre: the object is initialized. At least 1 relay port has this user
        port added to its port list
        Post: listens for information over this node's port
        Prints received info."""
        thread.start_new_thread(self.listenThread,())
    
    def send(self, info):
        """Pre: nearby relay node is listening for data
        Post: sends info to the nearby relay node"""
        #print "Sending message..."
        msgID = ""
        for i in range(1,8):
            msgID = msgID+chr(random.randint(0,255))
        sendAddress = (self.host, self.relayPort)
        self.sock.sendto(msgID+info, sendAddress)
        