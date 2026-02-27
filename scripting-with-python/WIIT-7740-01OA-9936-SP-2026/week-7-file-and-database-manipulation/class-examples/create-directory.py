import os

directory = 'xml'
parent_dir = "C:/Users/ancs2/PycharmProjects/cscc/scripting-with-python/WIIT-7740-01OA-9936-SP-2026/week-7-file-and-database-manipulation/class-examples"
# giving read/write permission to owner and user
mode = 666

path = os.path.join(parent_dir, directory)

print(path)
# os.mkdir(path, mode)
os.chmod(path, mode)