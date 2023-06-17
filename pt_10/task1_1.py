# game hangman
import random
import csv
def hangman(word):
    wrong = 0
    stages = [
        "",
        "________        ",
        "|               ",
        "|       |       ",
        "|       0       ",
        "|      /|\      ",
        "|      / \      ",
        "|               ",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Добро пожаловать на казнь")

    while wrong < len(stages) - 1:
        print()
        char = input("Введите букву: ")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e=wrong+1
        print("\n".join(stages[:e]))
        #winning condition
        if "_" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win=True
            break
    #losing condition
    if not win:
        print("\n".join(stages[:wrong]))
        print(f"Вы проиграли! Было загадано слово:{word}")
# game starts
# here that program tries to take words from csv(comma separated) file 
wordlist=[]
with open("hangman_word_list.csv","r") as csvfile:
    w=csv.reader(csvfile,delimiter=",")
    for str in w:
        wordlist.append(str)
if list.__len__(wordlist)!=0:
    hangman(random.choice(wordlist)[0])
else:
    hangman("крот")