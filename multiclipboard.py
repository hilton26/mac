import sys
import clipboard
import json

# check if user passed only one command
if len(sys.argv) ==2:
    command = sys.argv[1]
    print(command)
    
    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("Please enter exactly one command.")
        
