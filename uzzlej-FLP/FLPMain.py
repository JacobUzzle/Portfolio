# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:10:17 2016

@author: uzzlej
Purpose:
To play a game with the user wherein they have to find the exit room. The user chooses a 1 or a 2 to progress,
and can meet dead ends. They can also save their file at any time.
Special Thanks to Jan Pearce for use of the Stack class.
"""
import os
import room

def clear():
    os.system('cls')

def game(player):
    """Helper to keep the main method a bit cleaner"""
    while(True):
        if(player.atExit()):
            choice = loopinput(player.draw()+"\nWhat do you do?\nType exit to leave!","Too bad! You can't do that.",["exit","save","quit","1","2","back"])
        else:
            choice = loopinput(player.draw()+"\nWhat do you do?","Too bad! You can't do that.",["save","quit","1","2","back"])
        if(choice == "save"):
            filename = raw_input("What do you want to save as? (omit .txt extension).")
            player.save("Saves\\"+filename+".txt")
            clear()
        elif(choice == "quit"):
            choice1 = loopinput("Are you sure? (y/n)","Are you sure (y/n)",["y","yes","n","no"])
            #If they say yes, leaves the game via return
            if(choice1[0] == "y"):
                print("The Way of Doors awaits your return...")
                return
        elif(choice == "1" or choice == "2"):
            if(player.door(int(choice)) != None):#Move the hero into the next room
                print("You move into the next room.")#This method will not if it is empty
            else:
                if (player.atExit() != True):
                    print("You run into a solid wall.")
                    print("Way to go.")
                else:
                    print("Type exit to leave, please!")
                
        elif(choice == "back"):
            if(player.goBack()):
                print("You go back to the last room you were in.")
            else:
                print("The beginning is not the way out...")
                print("You run into a solid wall.")
                print("Way to go.")
        if(choice == "exit"):
            print("Congratulations! You left!")
            print("You find yourself magically transported back home.")
            print("At least, for now...")
            print("Press enter to return to the menu.")
            raw_input()
            clear()
            return
        
            
        
    
def loopinput(string, errstring, val_list):
    """Pre: val_list is a list of strings, string is a string to be printed,
    errstring is a string to be printed if the input string is not in val_list
    Post: continually prompts the user for using string for a value until 
    their input is inside of the list of strings."""
    userinput = raw_input(string)
    clear()
    while(userinput not in val_list):
        print(errstring)
        userinput = raw_input(string)
        clear()
    return userinput
        
def main():
    keepMenu = True
    errstring1 = "Please type a 1 or 2"
    room_map = room.RoomMap()
    player = room.Adventurer(room_map)
    
    while(keepMenu):
        print("Welcome to the Way of Doors!")
        input1 = loopinput("Enter 1 to learn the rules, enter 2 to explore.\nType quit to quit.", errstring1, ["1","2","quit"])
        clear()
        if(input1 == "1"):
            print("Type 1 or 2 to take the corresponding door on the screen.")
            print("Type save at any time to save the current game.")
            print("Type back to go to a previous room.")
            print("Try to find the exit! You win the game if you reach it.")
            print("The depth of the maze increases its size.")
            raw_input("Enter to go back to the menu.")
            clear()
        elif(input1 == "2"):
            input2 = loopinput("Enter 1 to load, enter 2 to start a new game.", errstring1, ["1","2"])
            #If the file exists, load it. Otherwise, loop go back through the loop
            if(input2 == "1"):
                while(True):
                    try:
                        filename = raw_input("What is the filename for your save? (omit .txt extension)")
                        clear()
                        player.load("Saves\\"+filename+".txt")
                        break
                    except:
                        print("Hmm.. There was an error loading the file.")
                        print("Please try again.")
                        
                    
                print("You are transported back to where you were,")
                print("a lost soul in the mysterious Way of Doors...")
                
                game(player)
            elif(input2 == "2"):
                while(True):
                    try:
                        depth = int(raw_input("What is the maximum length of the dungeon you want?"))
                        clear()
                        if(depth == 0):#We should not have a dungeon of size 0
                            raise Exception
                        break
                    except:
                        print("Please type in an integer greater than 0.")  
                clear()
                room_map = room.RoomMap()
                room_map.seed(depth)
                print("You are transported to the mysterious Way of Doors...")
                player = room.Adventurer(room_map)
                game(player)
        elif(input1 == "quit"):
            print("Goodbye.")
            return
            
main()