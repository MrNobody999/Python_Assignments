    # 4. Design automation script which accept directory name and delete all duplicate files from that directory. 
    # Write names of duplicate files from that directory into log file named as Log.txt.
    # Log.txt file should be created into current directory. Display execution time required for the script.

        # Usage : DirectoryDuplicateRemoval.py “Demo”
    # Demo is name of directory.

import sys
import os
import hashlib
import time

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()

    return hobj.hexdigest()

def DeleteDuplicates(DirName):
    if not os.path.exists(DirName):
        print("Error: Invalid Path")
        return

    dups = {}
    for FolderName, SubFolder, Filename in os.walk(DirName):
        for fname in Filename:
            path = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(path)
            
            if checksum:
                if checksum in dups:
                    dups[checksum].append(path)
                else:
                    dups[checksum] = [path]

    log_file = "Log.txt"
    deleted_count = 0
    
    with open(log_file, "w") as f:
        f.write("-" * 70 + "\n")
        f.write(f"Duplicate Removal Log: {time.ctime()}\n")
        f.write("-" * 70 + "\n")

        for checksum, files in dups.items():
            if len(files) > 1:
                for file_to_delete in files[1:]:
                    try:
                        os.remove(file_to_delete)
                        f.write(f"Deleted: {file_to_delete}\n")
                        deleted_count += 1
                    except Exception as e:
                        f.write(f"Error deleting {file_to_delete}: {e}\n")

    print(f"Log file 'Log.txt' created successfully.")
    print(f"Total duplicate files deleted: {deleted_count}")

def main():
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Usage : DirectoryDuplicateRemoval.py <Directory_Name>")
        return

    try:
        DeleteDuplicates(sys.argv[1])
    except Exception as e:
        print(f"An error occurred: {e}")

    end_time = time.time()
    
    print("-" * 30)
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    print("-" * 30)

if __name__ == "__main__":
    main()