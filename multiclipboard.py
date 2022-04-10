## This is the main file 

import sys
import clipboard
import json


#* Create a function that takes a json file and some type of 'data' as its 2 parameters
#* Opens the json mode in write('w') mode and writes the contents of the data parameter to the file
def save_items(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)


#* Create a function that takes a json file as its only parameter, opens it, and returns 
#* the contents of the file as a list of dictionaries
def load_items(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        return data


#* This variable will store the contents of the clipboard into a variable to be saved
#* if the user selects the 'save' option when using the program
SAVED_DATA = "clipboard.json"


if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items('clipboard.json', data)
        
    elif command == "load":
        print("Load function works")

    elif command == "list":
        print("list function works")
    else:
        print("Unknown Command, Please enter save , load, or list")
     
    


