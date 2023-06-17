##1st question. Split word into symbols. Dumb solution
#some_text="Чехов"
#print(some_text[0])
#print(some_text[1])
#print(some_text[2])
#print(some_text[3])
#print(some_text[4])
##2nd question. 2 strings from user into one
#first_string=input("Введите первую строку!")
#second_string=input("Введите вторую строку!")
#print("Вчера я написал {}. Вчера я ходил в {}!".format(first_string,second_string))
##3rd question. capitalize text
#first_string="олдос Хаксли родился в 1894 году."
#print(first_string.capitalize())
##4-th question. Text into array/set_of_text
#string="Где это? Кто это? Когда это?"
#print(string.split("? "))
##5-th question. array/set_of_text into Text
#set_of_text=["Рыжая","лиса","перепрыгнула","через","низкий","забор","."]
#new_string=" ".join(set_of_text)
#new_string=new_string.replace(" .",".")
#print(new_string)
##6-th question. Replacing symbols in a text
#replacing_symbol="о"
#string="Ребёнок - зеркало поступков родителей."
#new_string=string.replace(replacing_symbol,"0")
#print(new_string)
##7-th question. Indexing 1st entry of searching pattern
#searching_symbol="м"
#string="Хемингуэй"
#new_string=string.index(searching_symbol)
#print(new_string)
##8-th question. Make my favourite string immortal.
#replacing_symbol="\""
#string="\"По мере нагрева его меч может принимать разные агрегатные состояния. При самых высоких температурах лезвие становится плазмой. Артур создаёт плазму, раскаляя меч, и стреляет ею. В общем, он использует очень горячий и плотный клинок\""
#new_string=string.replace(replacing_symbol,"")
#print(new_string)
##9-th question. Multiple string or make it with 3 different words
#string="три"
#print(string+string+string+string+string+string+string)
#print(string*3)
#10-th question. Slice part of the text.
string="И незачем так орать! Я и в первый раз прекрасно расслышал."
print(string[:string.index("!")+1])
