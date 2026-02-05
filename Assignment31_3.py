# Design automation script which accept two directory names. Copy all files from first directory
# into second directory. Second directory should be created at run time.
    # Usage : DirectoryCopy.py "Demo" "Temp"
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files from Demo to Temp.

import sys
import os
import shutil

def NewDir(source_dir, destination_dir):

    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    try:
        os.makedirs(destination_dir, exist_ok=True)
        print(f"Destination directory '{destination_dir}' created (if needed).")
    except OSError as e:
        print(f"Error creating destination directory '{destination_dir}': {e}")
        return

    try:
        for foldername, subfolders, filenames in os.walk(source_dir):
            for filename in filenames:
                source_path = os.path.join(foldername, filename)
                
                relative_path = os.path.relpath(foldername, source_dir)
                destination_path = os.path.join(destination_dir, relative_path, filename)
                
                destination_subfolder = os.path.dirname(destination_path)
                if not os.path.exists(destination_subfolder):
                    os.makedirs(destination_subfolder, exist_ok=True)

                shutil.copy2(source_path, destination_path)
                print(f"Copied: '{source_path}' to '{destination_path}'")
        print("File copying process complete.")

    except shutil.Error as e:
        print(f"Error during file copying: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        print("Usage: python DirectoryCopy.py <SourceDirectoryName> <DestinationDirectoryName>")
        print("Example: python DirectoryCopy.py Demo Temp")
        return

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    
    NewDir(source_directory, destination_directory)


if __name__ == "__main__":
    main()
