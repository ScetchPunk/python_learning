#shows= ["Во все тяжкие","Секретные материалы","Фарго"]
#for show in shows:
#    print(show)
#
#coms= ("Теория большого взрыва","Друзья","Папины дочки")
#for show in coms:
#    print(show)
#
#people= {"Джим Парсонс":"Теория большого взрыва","Брайан Крэнстон":"Breaking bad","Екатерина Старшова":"Папины дочки"}
#for character in people:
#    print(character)
#
#tv=["Во все тяжкие","Секретные материалы","Фарго"]
#i=0
#for show in tv:
#    new=tv[i]
#    new=new.upper()
#    tv[i]=new
#    i+=1
#print(tv)

tv=["Во все тяжкие","Секретные материалы","Фарго"]
i=0
for i, show in enumerate(tv):
    new=tv[i]
    new=new.upper()
    tv[i]=new
print(tv)
