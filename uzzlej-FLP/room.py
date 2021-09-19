# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:02:45 2016

@author: Jacob  Uzzle
"""
import random
from Stack import *
class Room():
    RANDOM_PART1 = ["","","circular","slanted","purple","blue","red","yellow","green","bright", "orange",""]
    RANDOM_PART2 = ["hot","cold","smelly","normal","dark","crowded","tiny","large"]
    RANDOM_PART3 = [" with a swimming pool."," covered with mildew."," filled with rabbits."," with a grass floor."," decorated with party streamers.",".","."]
    RANDDOOR_PART1 = ["normal","decrepit","massive","beautiful","purple","bamboo","brown"]
    RANDDOOR_PART2 = [" marked with an A."," marked with a B."," with a picture of a happy face."," with a picture of a sad face.",".","."]

    def __init__(self):
        """Extension of the Room class. Contians a link to two more rooms,
        a value representing its description, and two values representing the
        doors. If this is the exit, isExit will be true. A room must either have
        TWO doors or no doors.
        """
        self.room_description = ""
        self.link_1 = None
        self.link_2 = None
        self.door_1 = "This is just a wall."
        self.door_2 = "This is just a wall."
        self.isExit = False
        
    def draw(self):
        """Pre: the room has a description
	Post: Returns a string based off the description. Gives a different description
     if the room is the exit. Draws the two doors after the description"""
        if(self.isExit):
            return self.room_description+"\nYou see the exit door!"
        else:
            if(self.link_1 == None and self.link_2 == None):
                return self.room_description+"\nThis is a dead end."
            else:
                return self.room_description+"\n1. "+self.door_1+"\n2. "+self.door_2
    
    def seed(self):
        """Pre: the room has been instantiated
	Post: Makes the description for the room and the doors"""
        rand1 = random.randrange(0, len(self.RANDOM_PART1))
        rand2 = random.randrange(0, len(self.RANDOM_PART2))
        rand3 = random.randrange(0, len(self.RANDOM_PART3))
        
        #Below are a few selections to clean up the seed
        if(self.RANDOM_PART1[rand1] == ""):
            #if it is empty, get rid of the extraneous space.
            self.room_description = "A "+self.RANDOM_PART2[rand2]+" room"+ self.RANDOM_PART3[rand3]
        else:
            if(self.RANDOM_PART1[rand1][0] in "aeiou"):#If the word begins with a value, use "an"
                self.room_description = "An "+self.RANDOM_PART1[rand1]+" "+self.RANDOM_PART2[rand2]+" room"+ self.RANDOM_PART3[rand3]
            else:
                self.room_description = "A "+self.RANDOM_PART1[rand1]+" "+self.RANDOM_PART2[rand2]+" room"+ self.RANDOM_PART3[rand3]
        randdoor1 = random.randrange(0,len(self.RANDDOOR_PART1))
        #Simple random statements to create an interesting string from the
        #class lists.
        randdoor1 = random.randrange(0,len(self.RANDDOOR_PART1))
        randdoor2 = random.randrange(0,len(self.RANDDOOR_PART2))
        self.door_1 = "A "+self.RANDDOOR_PART1[randdoor1]+" door"+self.RANDDOOR_PART2[randdoor2]
        randdoor1 = random.randrange(0,len(self.RANDDOOR_PART1))
        randdoor2 = random.randrange(0,len(self.RANDDOOR_PART2))
        self.door_2 = "A "+self.RANDDOOR_PART1[randdoor1]+" door"+self.RANDDOOR_PART2[randdoor2]
    
    def nextRoom(self, value):
        """Pre: value is an integer
        Post: returns link 1 if value is odd, link 2 if even."""
        if(value % 2 == 0):
            return self.link_2
        else:
            return self.link_1
        
    def drawDoor(self, value):
        """Pre: value is an integer
        Post: returns the door 1 description if value is odd, door 2 if even."""
        if(self.link_1 == None and self.link_2 == None):
            return "This is a dead end. Turn back!"
        if(value % 2 == 0):
            return self.door_2
        else:
            return self.door_1
            
    def saveString(self):
        """Pre: the room has been instantiated
        Post: returns a string for saving in the following fashion:
    	Room:
	<room description>
	<string saying “Dead End” if this is a dead end, or “Exit” if it is the exit>
	Door 1:
	<door description>
	Door 2:
	<door description>
        """
        string = ""
        string += "Room:\n"
        string += self.room_description+"\n"
        if(self.link_1 == None and self.link_2 == None):
            if(self.isExit):
                string += "Exit\n"
            else:
                string += "Dead End\n"
        else:
            string += "Door 1:\n"
            string += self.door_1+"\n"
            string += "Door 2:\n"
            string += self.door_2+"\n"
        return string
        
    def getisExit(self):
        """Pre: the room has been instantiated
        Post: returns true if the room is an exit, false otherwise."""
        return self.isExit
        
class RoomMap(object):
    def __init__(self):
        """Purpose: contains a group of rooms with links to one another and a maximum
        depth that is zero until the room is seeded
        Seed randomly creates the map with a reachable exit at a specified
        depth."""
        self.root = Room()
        self.max_depth = 0
        
    def getRoot(self):
        """Returns the root of this map"""
        return self.root
        
    def load(self, f):
        """Pre: f is a file object that exists
        Post: Reads the string at the location filename. 
        Creates the Binary tree based off the assignment’s specifications.
        The file is  closed after finishing."""
        
        self.root = self.treeBuilder(f, self.root)
        f.close()
        
    def write(self, f):
        """Pre: f is a file object that exists
        Post: writes based off the save file's specifications
        a file readable by the tree.
        The file is closed after finishing."""
        
        f.write(self.treeWriter(self.root, ""))
        f.close()
        
    def treeBuilder(self, full_file, temproot):
        """Pre: full_string is a file formatted according to assignment
        specifications
        Post: constructs the class based off this string."""
        string = ""
        while(True):
            try:
                string = full_file.readline() #Base case if the program has reached the end of the file
            except:
                return
            if("Room" in string):#End the looping if a room is reached
                break
            
        if("Room" in string):
            temproot = Room()#Create a new node to put the room in
            #ITS VERY IMPORTANT TO REMOVE THE NEWLINE CHARACTERS.
            temproot.room_description = full_file.readline().replace("\n","")
            #Read the door formatting
            first_string = full_file.readline()
            if(("Dead End" not in first_string) and ("Exit" not in first_string)):
                temproot.door_1 = full_file.readline().replace("\n","")
                full_file.readline()
                temproot.door_2 = full_file.readline().replace("\n","")
    #            temproot = temp_linknode
                temproot.link_1 = self.treeBuilder(full_file, temproot.link_1)
                temproot.link_2 = self.treeBuilder(full_file, temproot.link_2)
            
            if("Exit" in first_string):#Sets the room to the exit if the exit is reached.
                temproot.isExit = True
        return temproot
        
            
    def treeWriter(self, temproot, string = ""):
        """Pre: temproot is the head of a sub-branch
        Post: writes a formatted string based off the class."""
        
#        temp_string = "Room:\n"
#        temp_string += temproot.room_description+"\n"
        temp_string = temproot.saveString()
        if(temproot.link_1 == None or temproot.link_2 == None): #Base case: if it is a dead end
#            if(temproot.isExit):
#                temp_string += "Exit\n"
#            else:
#                temp_string += "Dead End\n"
            string += temp_string
            return string
        else:
#            temp_string += "Door 1:\n"+temproot.door_1+"\n"
#            temp_string += "Door 2:\n"+temproot.door_2+"\n"
            string += temp_string
            string = self.treeWriter(temproot.link_1, string)#Go down the door 1 route
            string = self.treeWriter(temproot.link_2, string)#Go down the door 2 route
            return string
    
    def seed(self, max_depth):
        """Pre: this is a new map that has not been loaded from a file
        Post: creates a map of maximum depth max_depth. Each room has a 1/8 chance
        of being a dead end. Each room is seeded according to the room 
        seed method. The rooms at the maximum depth are either dead ends or
        an exit. Randomly goes through the rooms and creates an exit at a dead end
        after seeding. Rooms below a depth of 2 are not made into Dead Ends."""
        self.max_depth = max_depth
        self.root = self.seedHelper(0, max_depth, 2, self.root)
        self.createExit(self.root)
        
    def seedHelper(self, depth, max_depth, min_depth, temproot):
        """Pre: this is a new map that has not been loaded from a file. Depth is
        a value of zero. max_depth is an integer, and so is min_depth
        Post: creates a map of maximum depth max_depth. Each room has a 1/4 chance
        of being a dead end. Each room is seeded according to the room 
        seed method. Rooms below min_depth are not randomly assigned as dead
        ends. The rooms at the maximum depth are either dead ends or
        an exit. Returns the root with all of the completed references."""
        #Part for BIG O analysis
        rand = random.randrange(0,4)
        temproot.seed()
        if(depth < max_depth):
            if(rand > 0 or depth < min_depth):#Random chance that the room will be a dead end.
                room1 = Room()
                room2 = Room()
                temproot.link_1 = self.seedHelper(depth+1, max_depth, min_depth, room1)
                temproot.link_2 = self.seedHelper(depth+1, max_depth, min_depth, room2)
            else:
                temproot.link_1 = None
                temproot.link_2 = None
        else:#Base case: if the maximum depth has been reached
            temproot.link_1 = None
            temproot.link_2 = None
        return temproot
        

    def createExit(self, temproot):
        """Pre: this is a fully fleshed-out map without an exit
        Post: Randomly goes through the rooms and creates an exit at a dead end
        after seeding."""
        if(temproot.link_1 == None or temproot.link_2 == None):#Base case: if this is a dead end.
            temproot.isExit = True
        else:
            rand = random.randrange(0,2)
            self.createExit(temproot.nextRoom(rand))#Move down a random branch
            

class Adventurer():
    def __init__(self, game_map = None):
        """Pre: game_map is a fully created map with at least a root and an exit.
        Directions are a series of 1's and 0's detailing the adventurer's current
        position. They are removed as the adventurer moves back through a door,
        and added as they go through door 1 or door 2."""
        self.directions = ""
        self.level = 10
        self.depth = 0#Current depth of the hero on the room map tree.
        self.room_stack = Stack()
        self.map = game_map
        if(game_map != None):#If the current map is not empty,
            self.room_stack.push(self.map.getRoot())#The hero starts out in the first room on the map
        
        
    def draw(self):
        """Pre: the user is on a non-empty map
        Post: returns a string of the user's current location with a choice of
        doors. """
        return self.room_stack.top().draw()#Return the description of the current room
        
    def door(self, doornum):
        """	Pre: the hero is inside a room, doornum is an integer.
	Post: updates the current room link to the room through the first door if 
     doornum is odd, or the room through the second door if doornum is even. 
     Pushes this onto the stack. If the room does not exits,
     the hero is not advanced. Returns the room to move into if the next room exists,
     returns None if it does not."""
        curr_room = self.room_stack.top()
        if(curr_room.nextRoom(doornum) != None):#If this is a dead end, push the room onto the stack
            self.room_stack.push(curr_room.nextRoom(doornum))
            self.directions += str(doornum % 2)
            self.depth += 1
            return curr_room
        else:
            return None
            
    def goBack(self):
        """Pre: the adventurer has a nonempty room stack
        Post: pops the current room off the stack, and removes the last move
        from the directions string. Returns True if the adventurer could go
        back, False if they were at a depth of 0."""
        if(self.depth != 0):
            self.room_stack.pop()
            self.depth -= 1
            self.directions = self.directions[0:-1]
            return True
        else:
            return False
        
    def atExit(self):
        """Pre: the adventurer is on a room map
        Post: returns true if the adventurer is at an exit room."""
        return self.room_stack.top().getisExit()
        
    def save(self, filename):
        """Pre: the adventurer is on a map with at least a seeded root node
        filename is a string representing a file location
        Post: writes a file according to these specifications for loading:
      Position:
	<string of ones and twos>
	Dungeon:
	Room:
	<room description>
	<string saying “Dead End” if this is a dead end, or “Exit” if it is the exit>
	Door 1:
	<door description>
	Door 2:
	<door description>
	Room:
	<description of room behind door 1>
	<repeat formatting until the room says “Dead End” or “Exit”>
	Room:
	<description of room behind door 2>
"""
        f = file(filename, "w")
        f.write("Position:\n")
        f.write(self.directions+"\n")
        f.write("Dungeon:\n")
        self.map.write(f)
        
    def load(self, filename):
        """Pre: the adventurer is on an unseeded map.
        filename is a string representing a file location
        Post: loads a file according to save specifications."""
        f = file(filename, "r")
        f.readline()#Header saying "Position:"
        tempdirections = f.readline().replace("\n","")
        f.readline()#Line that says "Dungeon:"
        self.map.load(f)#Add the map to the end of the file.
        self.room_stack.push(self.map.getRoot())#The hero starts out in the first room on the map
        if(tempdirections != ""):
            for i in tempdirections:#Simulate the directions to the hero's
                self.door(int(i))#current location
            
    def getDepth(self):
        """Post: returns the depth of the adventurer on the map.
        This is the number of rooms it is down the map."""
        return self.depth
    def getLevel(self):
        """Post: returns the number of cards the adventurer has in battle."""
        return self.level
    
    def setLevel(self, value):
        """Pre: value is an integer
        Post: sets the level of the adventurer to value"""
        self.level = value
def tester():
    #Room map testing
    testmap1 = RoomMap()
    file1 = file("testmap1.txt", "r")
    testmap1.load(file1)
    print(testmap1.root.draw())
    print(testmap1.root.link_1.draw())
    print(testmap1.root.link_2.draw())
    print(testmap1.root.link_2.link_1.draw())
    
    file2 = file("testmap2.txt", "r")
    testmap2 = RoomMap()
#    testmap2.seed(3)
#    testmap2.write("testmap2.txt")
#    print(testmap2.root.room_description)
    testmap2.load(file2)
    print("Map has loaded.")
    #Room testing
    room = Room()
    room.seed()
    print(room.room_description)
    print(room.door_1)
    print(room.door_2)
    
    #Adventurer testing
    print("Adventurer testing")
    adv = Adventurer(testmap2)
    print(adv.draw())
    adv.door(2)
    print(adv.draw())
    adv.door(2)
    print(adv.draw())
    print(adv.directions)
    adv.goBack()
    print(adv.draw())
    print(adv.directions)
    adv.door(1)
    print(adv.draw())
    print(adv.directions)
    adv.door(2)
    print(adv.draw())
    print(adv.directions)
    adv.door(1)
    print(adv.draw())
    print(adv.directions)
    adv.goBack()
    print(adv.draw())
    print(adv.directions)
    
    testmap3 = RoomMap()
    testmap3.seed(5)
    print(testmap3.getRoot().saveString())
    adv2 = Adventurer(testmap3)
    adv2.door(1)
    adv2.door(2)
    adv2.door(1)
#    adv2.save("Saves\\testadv1.txt")
    adv2.load("Saves\\testadv1.txt")
    print(adv2.draw())
    
    
    
if __name__ == "__main__":    
    tester()
    