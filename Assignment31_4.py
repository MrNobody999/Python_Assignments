# Design automation script which accept two directory names and one file extension. Copy all
# files with the specified extension from first directory into second directory. Second directory
# should be created at run time.
    # Usage : DirectoryCopyExt.py "Demo" "Temp" ".exe"
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files with extension .exe from Demo to Temp.

import sys
import os
import shutil

def CopyFilesByExt(source_dir, destination_dir, file_extension):

    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist or is not a directory.")
        return

    if not file_extension.startswith('.'):
        file_extension = '.' + file_extension
        
    try:
        os.makedirs(destination_dir, exist_ok=True)
        print(f"Destination directory '{destination_dir}' ensured to exist.")
    except OSError as e:
        print(f"Error creating destination directory '{destination_dir}': {e}")
        return

    copied_count = 0
    try:
        for foldername, subfolders, filenames in os.walk(source_dir):
            for filename in filenames:
                if filename.endswith(file_extension):
                    source_path = os.path.join(foldername, filename)
                    
                    relative_path = os.path.relpath(foldername, source_dir)
                    destination_path = os.path.join(destination_dir, relative_path, filename)
                    
                    destination_subfolder = os.path.dirname(destination_path)
                    if not os.path.exists(destination_subfolder):
                        os.makedirs(destination_subfolder, exist_ok=True)

                    shutil.copy2(source_path, destination_path)
                    print(f"Copied: '{source_path}' to '{destination_path}'")
                    copied_count += 1

        print("-" * 40)
        print(f"File copying process complete. Total files copied: {copied_count}.")

    except shutil.Error as e:
        print(f"Error during file copying: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    if len(sys.argv) == 4:
        source_dir = sys.argv[1]
        destination_dir = sys.argv[2]
        file_extension = sys.argv[3]
        CopyFilesByExt(source_dir, destination_dir, file_extension)
    else:
        print("Invalid number of arguments.")
        print("Usage: python DirectoryCopyExt.py <SourceDirectoryName> <DestinationDirectoryName> <FileExtension>")
        print("Example: python DirectoryCopyExt.py \"Demo\" \"Temp\" \".exe\"")
        sys.exit(1)

if __name__ == "__main__":
    main()
