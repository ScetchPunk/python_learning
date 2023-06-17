qs=["what is your name?",
        "what is your favourite color?",
        "what are you doing?"]
n=0
while True:
    print("Введи X для выхода")
    a = input(qs[n])
    if a == "X":
        break
    n= (n+1)%3
