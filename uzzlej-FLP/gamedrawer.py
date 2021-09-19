# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 15:31:37 2016

@author: uzzlej
"""
import os

def GameDrawer():
    def __init__(self):
        """Post: creates a gamedrawer object"""
    
    def clear(self):
        """Post: clears the strings from the screen"""
        os.system('cls')
    
    def loopinput(self, string, errstring, val_list):
        """Pre: val_list is a list of strings, string is a string to be printed,
        errstring is a string to be printed if the input string is not in val_list
        Post: continually prompts the user for using string for a value until 
        their input is inside of the list of strings."""
        userinput = raw_input(string)
        self.clear()
        while(userinput not in val_list):
            print(errstring)
            userinput = raw_input(string)
            self.clear()
        return userinput
    
    def drawstring(self,string):
        """Pre: string is of type str
        Post: draws string on the screen"""
        print(string)
        
    def getInput(self, prompt):
        """Pre: prompt is of type str
        Post: gets input from the user"""
        returnstring = raw_input(prompt)
        self.clear()
        return returnstring