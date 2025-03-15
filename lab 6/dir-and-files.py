# task 1
import os

def list_contents(path):
    directories = []
    files = []
    
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
        elif os.path.isfile(full_path):
            files.append(item)

    print("Directories:", directories)
    print("Files:", files)
    print("All:", os.listdir(path))

path = "your_path_here"
list_contents(path)

# task 2
import os

def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

path = "your_path_here"
check_access(path)

# task 3
import os

def check_path(path):
    if os.path.exists(path):
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

path = "your_path_here"
check_path(path)

# task 4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        print("Number of lines:", sum(1 for _ in file))

file_path = "your_file.txt"
count_lines(file_path)

# task 5
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.writelines(f"{line}\n" for line in data)

data = ["line1", "line2", "line3"]
write_list_to_file("output.txt", data)

# task 6
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w') as file:
        pass

# task 7
def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())

copy_file("source.txt", "destination.txt")

# task 8
import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted.")
    else:
        print("File does not exist or cannot be deleted.")

delete_file("file_to_delete.txt")
