# Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

# Input
# Demo.txt

# Expected Output:
# Display each line of Demo.txt one by one.

import sys
import os


def PrintLines(FileName):
    fobj = open(FileName,"r")
    lines = fobj.readlines()
    for line in lines:
        print(line, end = " ")





def main():
    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print("Invalid number of arguments")
        return
    
    if len(sys.argv) > 1:
        FileName = sys.argv[1]

    if os.path.isfile(FileName) == False:
        print("File not exist.")
        return


    PrintLines(FileName)
    

if __name__ == "__main__":
    main()