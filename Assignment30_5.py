
# Search a Word in File
# Problem Statement :

    # Write a program which accepts a file name and a word from the user and checks whether that word is present in
    # the file or not.

    # Input:
    # Demo.txt Marvellous

    # Expected Output:
    # Display whether the word Marvellous is found in Demo.txt or not.

import sys
import os


def WordPresent(FileName, Word):
    fobj = open(FileName, "r")
    content = fobj.read()
    if Word in content:
        return True
    return False
    

def main():

    if len(sys.argv) < 0 or len(sys.argv) > 3:  
        print("Invalid number of arguments")
        return
    
    if len(sys.argv) > 1:
        FileName = sys.argv[1]

    if len(sys.argv) > 1:
        Word = sys.argv[2]

    if os.path.isfile(FileName) == False:
        print("File not exist.")
        return

    Ret = False
    
    Ret = WordPresent(FileName, Word)
    
    if Ret == True:
        print(f"Word {Word} is present in {FileName}.")
    else:
        print(f"Word {Word} is not present in {FileName}.")        


    
if __name__ == "__main__":
    main()