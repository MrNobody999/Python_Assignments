    # 3. Design automation script which accept directory name and delete all duplicate files from that directory. 
    # Write names of duplicate files from that directory into log file named as Log.txt.
    # Log.txt file should be created into current directory.

        # Usage : DirectoryDusplicateRemoval.py “Demo”
    # Demo is name of directory.
import sys
import os
import hashlib
import time

def CalculateChecksum(FileName):
    try:
        fobj = open(FileName, "rb")
        hobj = hashlib.md5()
        for chunk in iter(lambda: fobj.read(4096), b""):
            hobj.update(chunk)
        fobj.close()
        return hobj.hexdigest()
    except Exception as e:
        print(f"Could not read {FileName}: {e}")
        return None

def DeleteDuplicates(duplicates_dict):
    log_file_path = "Log.txt"
    separator = "-" * 70
    deleted_count = 0
    
    with open(log_file_path, "w") as log:
        log.write(f"{separator}\n")
        log.write(f"Duplicate Removal Log - {time.ctime()}\n")
        log.write(f"{separator}\n\n")

        for checksum, files in duplicates_dict.items():
            original = files[0]
            to_delete = files[1:]
            
            for file_path in to_delete:
                try:
                    os.remove(file_path)
                    log.write(f"DELETED: {file_path}\n")
                    deleted_count += 1
                except Exception as e:
                    log.write(f"ERROR: Could not delete {file_path} -> {e}\n")
        
        log.write(f"\n{separator}\n")
        log.write(f"Total files deleted: {deleted_count}\n")
        log.write(f"{separator}\n")
    
    return deleted_count

def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryDuplicateRemoval.py <DirectoryName>")
        return

    dir_name = sys.argv[1]

    if not os.path.isdir(dir_name):
        print(f"Error: {dir_name} is not a valid directory.")
        return

    print(f"Scanning directory: {dir_name}...")
    all_files = {}
    for folder, subfolders, filenames in os.walk(dir_name):
        for fname in filenames:
            path = os.path.join(folder, fname)
            checksum = CalculateChecksum(path)
            if checksum:
                all_files.setdefault(checksum, []).append(path)

    duplicates = {ck: paths for ck, paths in all_files.items() if len(paths) > 1}

    if not duplicates:
        print("No duplicate files found.")
        return

    print(f"Found {len(duplicates)} sets of duplicates. Cleaning up...")
    count = DeleteDuplicates(duplicates)
    
    print(f"Success! {count} files removed. Check 'Log.txt' for details.")

if __name__ == "__main__":
    main()
