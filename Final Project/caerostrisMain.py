# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 09:08:39 2018

@author: uzzlej
"""
import userNode
import relayNode
def main():
    U1 = userNode.userNode(1025,1026)
    U2 = userNode.userNode(1029,1027)
    A = relayNode.relayNode(1026)
    B = relayNode.relayNode(1027)
    C = relayNode.relayNode(1028)
    
    #A will be our access port for U1
    A.addPort(1027)
    A.addPort(1028)
    A.addPort(1025)
    
    #B will be our access port for U2
    B.addPort(1026)
    B.addPort(1028)
    B.addPort(1029)
    
    C.addPort(1027)
    C.addPort(1026)
    A.listen()
    B.listen()
    C.listen()
    U1.listen()
    
    U1.send("Hi!")
    U2.send("Hi!")
    U1.send("How are you?")
    U2.send("Good.")
    
main()
    