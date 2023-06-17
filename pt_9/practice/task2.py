askuser=input("В чём смысл жизни?\n")
with open("userAnswer.txt","w") as newfile:
    newfile.write(f'Q:В чём смысл жизни?\nA:{askuser}')