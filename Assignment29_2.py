# Display File Contents :

    # Problem Statement:
        # Write a program which aécepts a file name from the user, opens that file, and displays the entire contents on the console,

    # Input:
    # Demo.txt,

    # Expected Output:
    # Display contents of Demo. txt on console.

import sys
import os

def DisplayFile(FileName):
    FileData = open(FileName,"r")
    FileContent = FileData.read()
    return FileContent



def main():
    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print("Invalid number of arguments")
        return
    
    if len(sys.argv) > 1:
        FileName = sys.argv[1]

    if os.path.isfile(FileName) == False:
        print("File not exist.")
        return


    Ret = DisplayFile(FileName)
    print(Ret)
    

if __name__ == "__main__":
    main()