# Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extention.
    # Usage : DirectoryRename.py "Demo" ".txt" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc.

import sys
import os

def FileSearchExtention(DirectoryName, FileExtention1, FileExtention2):
    Ret = False
    
    Ret = os.path.exists(DirectoryName)
    if (Ret == False):
        print("There is no such directory")

    Result = []
    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            if fname.endswith(FileExtention1):
                Oldpath = os.path.join(FolderName,fname)
                NewName = fname.replace(FileExtention1, FileExtention2)
                NewPath = os.path.join(FolderName, NewName)

                try:
                    os.rename(Oldpath, NewPath)
                    print(f"Renamed : {Oldpath} to {NewPath}")
                except Exception:
                    print(f"Error renaming {Oldpath}: {Exception}")


                


def main():
    if len(sys.argv) != 4:
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return
    
    DirectoryName = sys.argv[1]
    FileExtention1 = sys.argv[2]
    FileExtention2 = sys.argv[3]
    
    
    FileSearchExtention(DirectoryName, FileExtention1, FileExtention2)


if __name__ == "__main__":
    main()