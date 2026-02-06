    # 2. Design automation script which accept directory name and write names of duplicate files from
    # that directory into log file named as Log.txt. Log.txt file should be created into current directory.

        # Usage : DirectoryDusplicate.py “Demo”
    # Demo is name of directory.

import sys
import os
import hashlib
import time

def CalculateChecksum(FileName):
    try:
        fobj = open(FileName, "rb")
    except FileNotFoundError:
        print(f"Error: {FileName} not found.")
        return None
    
    hobj = hashlib.md5()
    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirName):
    if not os.path.exists(DirName) or not os.path.isdir(DirName):
        print(f"Error: Directory '{DirName}' not found or is not a valid directory.")
        return None

    Duplicate = {}
    for FolderName, SubFolderName, Filename in os.walk(DirName):
        for fname in Filename:
            full_path = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(full_path)
            if checksum is not None:
                if checksum in Duplicate:
                    Duplicate[checksum].append(full_path)
                else:
                    Duplicate[checksum] = [full_path]
    
    duplicates_found = {checksum: files for checksum, files in Duplicate.items() if len(files) > 1}
    return duplicates_found

def WriteLog(duplicates):
    """Writes the names of duplicate files to Log.txt."""
    border = "-" * 68
    timestamp = time.ctime()
    log_file_path = "Log.txt"
    
    with open(log_file_path, "w") as fobj:
        fobj.write(border + "\n")
        fobj.write("This is a log file created by Automation script.\n")
        fobj.write(f"Timestamp: {timestamp}\n")
        fobj.write("This script finds duplicate files.\n")
        fobj.write(border + "\n")

        if not duplicates:
            fobj.write("No duplicate files found.\n")
        else:
            fobj.write("Duplicate files found:\n")
            for checksum, files in duplicates.items():
                fobj.write(f"\nChecksum (MD5): {checksum}\n")
                for file_path in files:
                    fobj.write(f"\t{file_path}\n")
        
        fobj.write(border + "\n")
    
    print(f"Duplicate file report written to '{log_file_path}'.")

def main():
    border = "-"*68
    print(border)
    print("------------- Automation Script -------------")
    print(border)
    
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        print("Usage: python DirectoryDuplicate.py" "Demo")
        sys.exit(1) 

    directory_name = sys.argv[1]
    
    duplicates_map = DirectoryWatcher(directory_name)
    
    if duplicates_map is not None:
        WriteLog(duplicates_map)

    print(border)
    print("------------- Automation Script -------------")
    print(border)

if __name__ == "__main__":
    main()
