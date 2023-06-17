import os

with open(os.path.join(os.path.expanduser("~"),"Documents","Music.txt"),"r") as file:
    print(file.read())