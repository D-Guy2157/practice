import os
import shutil

path = "folder"

try:
    os.remove(path)      # delete a file
    # os.rmdir(path)       # delete an empty directory
    # shutil.rmtree(path)  # delete a directory containing files
except FileNotFoundError:
    print(path + " was not found")
except PermissionError:
    print("Insufficient Permission")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")
