# Design automation script which accept directory name and file extension from user. Display all files with that extension.
# Usage : DirectoryFileSearch.py "Demo" ".txt"
# Demo is name of directory and .txt is the extension that we want to search.

import sys
import os

def FileSearchExtention(DirectoryName, FileExtention):
    Ret = False
    
    Ret = os.path.exists(DirectoryName)
    if (Ret == False):
        print("There is no such directory")

    Result = []
    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            if fname.endswith(FileExtention):
                fname = os.path.join(FolderName,fname)
                Result.append(fname)

    if len(Result) == 0:
        print(f"No files with extention '{FileExtention}' found.")
    else:
        print(f"Found {len(Result)} files: ")
        for file in Result:
            print(file)


def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return
    
    DirectoryName = sys.argv[1]
    FileExtention = sys.argv[2]
    
    FileSearchExtention(DirectoryName, FileExtention)


if __name__ == "__main__":
    main()