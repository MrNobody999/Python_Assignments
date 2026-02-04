# Frequency of a String in File : 

    # Problem Statement:
    # Write a program which accepts a file name and one string from the user and returns the frequency (count of
    # occurrences) of that string in the file.

    # Input
    # Demo.txt Marvellous

    # Expected Output:
    # Count how many times "Marvellous" appears in Demo. txt


import os
import sys

def StringCount(FileName, String1):
    fobj = open(FileName, "r")
    content = fobj.read()
    count = content.count(String1)
    print(f"Count of {String1} in {FileName} is : ", count)



def main():

    if len(sys.argv) < 0 or len(sys.argv) > 3:  
        print("Invalid number of arguments")
        return
    
    if len(sys.argv) > 1:
        FileName = sys.argv[1]

    if len(sys.argv) > 1:
        String1 = sys.argv[2]

    if os.path.isfile(FileName) == False:
        print("File not exist.")
        return

    
    StringCount(FileName, String1)
    
if __name__ == "__main__":
    main()