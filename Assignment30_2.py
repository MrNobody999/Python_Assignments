# Count Words in a File

    # Problem Statement:
    # Write a program which accepts/a file name from the user and €6unts the total number of words in that file.

    # Input
    # Demo.txt

    # Expected Output:
    # Total number of words in Demo.txt

import sys
import os


def WordsCount(FileName):
    fobj = open(FileName,"r")
    content = fobj.read()
    words = content.split()
    word_count = len(words)
    return word_count


def main():
    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print("Invalid number of arguments")
        return
    
    if len(sys.argv) > 1:
        FileName = sys.argv[1]

    if os.path.isfile(FileName) == False:
        print("File not exist.")
        return


    Ret = WordsCount(FileName)
    print(f"Number of words are present in {FileName} is : ",Ret)
    

if __name__ == "__main__":
    main()