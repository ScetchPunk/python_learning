def count_characters(string):
    count_dict={}
    string=string.lower()
    for char in string:
        if char in count_dict:
            count_dict[char]+=1
        else:
            count_dict[char]=1
    print(count_dict)
word=input("Введите сюда своё слово для подсчёта символов в нём:\n")
count_characters(word)