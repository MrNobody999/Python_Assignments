# 1.Design automation script which accept directory name and display checksum of all files.
    # Usage : DirectoryChecksum.py "Demo"
# Demo is name of directory.

import sys
import os
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirName):
    Ret = False

    Ret = os.path.exists(DirName)
    if (Ret == False):
        print("There is no such file.")
        return
    
    Ret = os.path.isdir(DirName)
    if (Ret == False):
        print("It is not a directory.")
        return


    for FolderName, SubFolder, Filename in os.walk(DirName):

        for fname in Filename:
            fname = os.path.join(FolderName, fname)
            Checksum = CalculateChecksum(fname)
            print(f"File name : {fname} Checksum : {Checksum}")



def main():
    if len(sys.argv) < 1 or len(sys.argv) > 2:
        print("Invalid number of arguments")
        return
    Directory = sys.argv[1]
    DirectoryWatcher(Directory)

if __name__ == "__main__":
    main()