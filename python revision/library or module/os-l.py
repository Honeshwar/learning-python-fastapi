import os

# os.getcwd(): Returns the current working directory.
print("current working directory",os.getcwd())

# os.listdir(path): Lists([]) files and directories in the specified path.
print(os.listdir())

# os.mkdir(path): Creates a new directory at the specified path.
if not os.path.exists("test"):
    print("created directory",os.mkdir("test"))
    print("deleted directory",os.rmdir("test"))

  

# os.remove(path): Deletes the file at the specified path.
# os.remove("test")

# os.rename(src, dst): Renames a file or directory from src to dst.
# print("renamed directory",os.rename("test","test1") )

# os.path.join(path, *paths): Joins one or more path components intelligently.
print(os.path.join("test1","test"))# test1/test

# os.path.exists(path): Checks if the path exists.
print('path exists',os.path.exists('./'+os.path.join("test1","test")))