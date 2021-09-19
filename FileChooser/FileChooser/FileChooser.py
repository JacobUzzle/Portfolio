import subprocess
import os
import random
import json
import tkinter
#A list of files used for selection
#TODO: Implement the ability to move forward/backward a given amount of indices on the list
#TODO: Implement some way to 'refresh' a list when new files have been added. This should be done by comparing the list before the refresh
#to the most recent folder. If any files have been deleted or renamed, remove that file from the list. If any new files are found, add them
#at random to the list. Make sure to update the current index so that if the item removed or added was before the current index, the current
#index is reduced by 1 or increased by 1.
#TODO: Give the user the ability to prevent certain folders from being added to the list (using name/attributes). 
#TODO: Give the user the ability to prevent certain file extensions from being added to the list
#TODO: Implement a feature that can open file shortcuts as normal folders. Duplicate folder shortcuts will not be opened
#Optionally, add the ability to add other folders to this list that aren't sub-folders to the current one
def main():
    load_question = ""
    while(load_question != "q"):
        load_question = input("Type 'l' to load a saved playlist, type 'n' for a new playlist, press 'q' to quit: ")
        if(load_question == "n"):
            folder_loc = input("Input a folder location: ")
            max_depth = int(input("Input a max depth: "))
            file_list = filelistmaker(folder_loc,max_depth)
            rand_list = []
            #Create a randoml-generated 
            while(len(file_list) > 0):
                    rand_index = random.randint(0,len(file_list)-1)
                    rand_list.append(file_list.pop(rand_index))
            current_file_index = 0
            user_command = ""
            openfile(rand_list[0])
            user_command = input("Type n for the next media. Type p for the previous. Type r to reshuffle.\nType e to exit this playlist. Type s to save your current session.\n")
            while user_command != "e":
                user_command = input()
                if user_command == "n" or user_command == "":
                    current_file_index = (current_file_index+1) % len(rand_list)
                    openfile(rand_list[current_file_index])
                elif user_command == "p":
                    current_file_index = (current_file_index-1) % len(rand_list)
                    openfile(rand_list[current_file_index])
                elif user_command == "r":
                    random.shuffle(rand_list)
                    current_file_index = 0
                    openfile(rand_list[0])
                elif user_command == "e":
                    print("Exiting to load menu.")
                elif user_command == "s":
                    savename = input("Write the save name:")
                    json.dump([current_file_index,rand_list], open(savename, "w"))
                else:
                    print("Type n for the next media. Type p for the previous. Type r to reshuffle.\nType e to exit this playlist. Type s to save your current session.\n")
        elif(load_question == 'l'):
            list_name = input("Load the name of the file: ")
            fileread = open(list_name,"r")
            savefile = json.load(fileread)
            rand_list = savefile[1]
            save_index = savefile[0]
        
            current_file_index = save_index
            user_command = ""
            openfile(rand_list[save_index])
            user_command = input("Type n for the next media. Type p for the previous. Type r to reshuffle.\nType e to exit this playlist. Type s to save your current session.\n")
            while user_command != "e":
                user_command = input()
                if user_command == "n" or user_command == "":
                    current_file_index = (current_file_index+1) % len(rand_list)
                    openfile(rand_list[current_file_index])
                elif user_command == "p":
                    current_file_index = (current_file_index-1) % len(rand_list)
                    openfile(rand_list[current_file_index])
                elif user_command == "r":
                    random.shuffle(rand_list)
                    current_file_index = 0
                    openfile(rand_list[0])
                elif user_command == "e":
                    print("Exiting to load menu.")
                elif user_command == "s":
                    savename = input("Write the save name:")
                    
                    json.dump([current_file_index,rand_list], open(savename, "w"))
                elif(user_command == 'u'):
                    print("Updating...")
                else:
                    print("Type n for the next media. Type p for the previous. Type r to reshuffle.\nType e to exit this playlist. Type s to save your current session.\n")
        elif(load_question == 'q'):
            print("Bye bye!")
        else:
            "lmao"
def testmain():
    #Comment
    folder_loc = input("Input a folder location: ")
    max_depth = int(input("Input a max depth: "))
    file_list = filelistmaker(folder_loc,max_depth)
    rand_list = []
    while(len(file_list) > 0):
        rand_index = random.randint(0,len(file_list)-1)
        rand_list.append(file_list.pop(rand_index))
    #openfile("C:\\Users\\Jacob\\Documents\\My Digital Editions\\Testfolder\\almightyloaf.webm")
    for i in rand_list:
        print (i)
    input()
def filelistmaker(folder_loc, max_depth):
    """Pre: folder_loc is a real folder location and max_depth is the depth of folders within folders you want to open within this context
    Post: returns a list of all file locations from the current directory and all sub-directories within max_depth
    (e.g. setting max_depth to 1 will open all files from all folders within this directory, setting it to 2 will open all files within 
    folders in those folders, and 3 will open folders in those, etc.)"""
    file_list = []
    #Add all files to the file list
    for j in os.listdir(folder_loc):
        #Check if the index is a directory, and if it is, add it to the file list
        if(os.path.isdir(folder_loc+"\\"+j) == False):
            file_list.append(folder_loc+"\\"+j)
    #reduce the max depth for the next iteration
    max_depth = max_depth - 1
    if(max_depth > -1):
        #for each of the contents of this folder
        for i in os.listdir(folder_loc):
            #if it is a directory
            if(os.path.isdir(folder_loc+"\\"+i)):
                #get the files that aren't folders and append them to this fileList
                #repeat the same process for the sub-folder if the current depth is still less than
                #the max depth
                for k in filelistmaker(folder_loc+"\\"+i,max_depth):
                    file_list.append(k)
    return file_list

def openfile(file_loc):
    os.startfile(file_loc, 'open')
main()