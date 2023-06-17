class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def compareFunc(a, b):
    return a is b


per1 = Person("Gorgeous", "male")
per2 = Person("Zhanna", "female")
per3 = per2
if compareFunc(per3, per2):
    print(f"{per3.name} и {per2.name} являются одним и тем же объектом!")
else:
    print(f"{per3.name} и {per2.name} не являются одним и тем же объектом!")
