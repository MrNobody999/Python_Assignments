# Compare Two Files (Command Line) :
    # Problem Statement:
    # Write a program which accepts two file names through command line arguments and compares the contents of both files.
        # If both files contain the same contents, display Success 
        # Otherwise display Failure

    # Input (Command Line):
    # Demo.txt Hello.txt

    # Expected Output:
    # Success OR Failure

import hashlib
import os
import sys

def CalculateChecksum(FileName):     
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(File1, File2):
    
    File1_Checksum = CalculateChecksum(File1)

    File2_Checksum = CalculateChecksum(File2)
    
    print(f"File name : {File1} Checksum : {File1_Checksum}")
    print(f"File name : {File2} Checksum : {File2_Checksum}")

    if File1_Checksum == File2_Checksum:
        print("Success")
    else:
        print("Failure")


def main():

    if len(sys.argv) < 0 or len(sys.argv) > 3:  
        print("Invalid number of arguments")
        return
    
    if len(sys.argv) > 1:
        FileName1 = sys.argv[1]

    if len(sys.argv) > 1:
        FileName2 = sys.argv[2]

    if os.path.isfile(FileName1) == False:
        print("File not exist.")
        return
    if os.path.isfile(FileName2) == False:
        print("File not exist.")
        return
    
    DirectoryWatcher(FileName1, FileName2)
    
if __name__ == "__main__":
    main()