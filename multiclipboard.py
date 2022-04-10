## This is the main file 

import sys
import clipboard
import json


#* This variable will store the contents of the clipboard into a variable to be saved
#* if the user selects the 'save' option when using the program

SAVED_DATA = "clipboard.json"


#* Create a function that takes a json file and some type of 'data' as its 2 parameters
#* Opens the json mode in write('w') mode and writes the contents of the data parameter to the file
def save_items(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)


#* Create a function that takes a json file as its only parameter, opens it in read('r') mode, and returns 
#* the contents of the file as a list of dictionaries
#* If no file is found it returns an empty dictionary
def load_items(file_name):
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}


#! The program only runs if there is 1 additional argument after the file name => python3 multiclipboard.py save OR load OR list.  
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA) # Loads the current content of our json file into a variable so we can later access or append to it

    if command == "save":   # EXAMPLE: python3 multiclipboard.py save
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print(f"Saved contents of clipboard! Access with key:  {key}")
        
    elif command == "load": # EXAMPLE: python3 multiclipboard.py load
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key]) # If the key is in the json file, the "value" of the key is copied to the clipboard
            print(f"Content stored under: {key} has been copied to the clipboard!")
        else:
            print("Key not found!")

    elif command == "list": # EXAMPLE: python3 multiclipboard.py list
        print(data)
    
else:
    print("Unknown Command, Please enter save , load, or list")
     
    


