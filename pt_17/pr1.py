import re

with open("zen.txt","r") as zenfile:
    text=zenfile.read()
    print(text)
    print(re.findall("Dutch",text,re.IGNORECASE))
