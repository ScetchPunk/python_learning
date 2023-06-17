some_text="Кот в шляпе."
print("Проверяемый текст: {}".format(some_text))
checking_word=input("Введите проверяемое слово: ")
if (checking_word in some_text):
    print("Слово '{}' есть в строке '{}'".format(checking_word,some_text))
else:
    print("Слово '{}' нет в строке '{}'".format(checking_word,some_text))

checking_word=input("Введите проверяемое слово: ")
if (checking_word not in some_text):
    print("Слово '{}' нет в строке '{}'".format(checking_word,some_text))
else:
    print("Слово '{}' есть в строке '{}'".format(checking_word,some_text))
