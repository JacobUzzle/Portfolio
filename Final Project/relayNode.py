# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:13:10 2018

@author: uzzlej

The purpose of this is to create a node that will broadcast all information
over a single strand. This will only occur on a single machine over the ports
The identifier for each sent message will only be the first 8 characters,
each assigned random values (though this will occur in only relay nodes)
. Since I do not have access to the proper channels,
this will have to do."""
import socket
import random
import thread
class relayNode:
    def __init__(self,p):
        self.port = p
        #These are the ports directly connected to this node
        #over which the information should be broadcast
        self.nearbyPorts = []
        #The max number of IDs received before removing the first
        #part of the list of IDs
        #This will act as a queue in a first in first out structure
        self.idAmount = 3
        self.idList = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a datagram socket (UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Make the socket reusable
        self.sock.setblocking(False) # Set socket to non-blocking mode
        self.host = '127.0.0.1'
        self.sock.bind((self.host, self.port))
    def listenThread(self):
        while True:
            try:
                message, address = self.sock.recvfrom(self.port)
                #print "Message received over port "+str(self.port)
                #The first 3 characters 
                msgID = message[:7]
                #If the message id is the same as a previously received
                #message, do not broadcast it
                
                if msgID not in self.idList:
                    self.idList.append(msgID)
                    if message:
                        self.broadcast(message)
                    if len(self.idList) > self.idAmount:
                        self.idList.pop(0)
            except:
                pass

    def addPort(self,p):
        """Pre: p is a port number
        Post: adds that port to the id list
        """
        self.nearbyPorts.append(p)
    def listen(self):
        """Pre: all nearby node ports have been added
        Post: listens for information over this node's access port
        Broadcasts duplicate information over all node links.
        Note that all received messages will have the first 3
        characters devoted to the unique message ID.
        This id will be added to the idList. If the idList has
        more elements than the id amount, the first element of
        idList will be removed"""
        thread.start_new_thread(self.listenThread,())
    
    def broadcast(self, info):
        """Pre: all nearby node ports have been added
        Post: broadcasts info over all nearby ports"""
        
        for i in self.nearbyPorts:
            
            sendAddress = (self.host, i)
            self.sock.sendto(info, sendAddress)
        