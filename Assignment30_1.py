# Count Lines in a File.

    # Problem Statement:
    # Write a program which accepts a file name from the user and counts how many lines are present in the file.

    # Input:
    # Demo.txt
    # Expected Output:
    # Total number of lines in Demo.txt.

import sys
import os


def LinesCount(FileName):
    fobj = open(FileName,"r")
    lines = fobj.readlines()
    line_count = len(lines)
    return line_count




def main():
    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print("Invalid number of arguments")
        return
    
    if len(sys.argv) > 1:
        FileName = sys.argv[1]

    if os.path.isfile(FileName) == False:
        print("File not exist.")
        return


    Ret = LinesCount(FileName)
    print(f"Number of lines are present in {FileName} is : ",Ret)
    

if __name__ == "__main__":
    main()