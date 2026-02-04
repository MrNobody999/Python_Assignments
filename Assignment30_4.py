# Copy File Contents into Another File

# Problem Statement:
    # Write a program which accepts two file names from the user.
        # First file is an existing file

        # Second file is a new file
# Copy all contents from the first file into the second file.

# Input:
    # ABC.txt Demo.txt

# Expected Output
# Contents of ABC.txt copied into Demo.txt.


import sys
import os

def CopyContent(FileName1, FileName2):
    FileData = open(FileName1,"r")
    FileContent = FileData.read()
    
    dobj = open(FileName2, "w")
    dobj.write(FileContent)

    print(f"Contents of {FileName1} copied into {FileName2}")


def main():
    if len(sys.argv) < 0 or len(sys.argv) > 3:  
        print("Invalid number of arguments")
        return
    
    if len(sys.argv) > 1:
        FileName1 = sys.argv[1]

    if os.path.isfile(FileName1) == False:
        print("File not exist.")
        return
    
    if len(sys.argv) > 2:
        FileName2 = sys.argv[2]


    CopyContent(FileName1,FileName2)
    

if __name__ == "__main__":
    main()