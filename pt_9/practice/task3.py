import csv

new_list = [
    ["Звёздные войны", "Терминатор", "Искусственный интеллект"],
    ["Дурак", "Матильда", "Левиафан"],
    ["Люди в чёрном", "Эволюция", "Я - робот"],
]

with open("movies.txt", "w") as movf:
    for sublist in new_list:
        w = csv.writer(movf, delimiter=",")
        w.writerow(sublist)

with open("movies.txt", "r") as movf:
    r = csv.reader(movf, delimiter=",")
    #my variation
    for row in r:
        for str in row:
            print(f"{str},", end="")
        print()
    # print(",".join(row)) - book example
