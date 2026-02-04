# Check File Exists in Current Directory : 

    # Problem Statement:
        # Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

    # Input:
    # Demo.txt

    # Expected Output:
    # Display whether Demo.txt exists or not.

import sys
import os

def main():

    if len(sys.argv) > 1:
        FileName = sys.argv[1]
        print(FileName)

        if os.path.isfile(FileName):
            print(f"{FileName} is exist.")
        else:
            print(f"{FileName} is not exist.")



if __name__ == "__main__":
    main()