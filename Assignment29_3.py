# Copy File Contents into a New File (Command Line) : 

    # Problem Statement
    # Write a program which accepts an existing file name through command line arguments, creates a new
    # named Demo.txt, and copies all contents from the given file into Demo.txt.

# Input (Command Line):
# ABC.txt

# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import sys
import os

def DisplayFile(FileName):
    FileData = open(FileName,"r")
    FileContent = FileData.read()
    
    dobj = open("Demo.txt", "w")
    dobj.write(FileContent)

    print(f"Contents of {FileName} copied into Demo.txt")


def main():
    if len(sys.argv) < 0 or len(sys.argv) > 2:  
        print("Invalid number of arguments")
        return
    
    if len(sys.argv) > 1:
        FileName = sys.argv[1]

    if os.path.isfile(FileName) == False:
        print("File not exist.")
        return


    DisplayFile(FileName)
    #print(Ret)
    

if __name__ == "__main__":
    main()