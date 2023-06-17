import csv

wordlist=[]
def ask_user_for_words():
   isAsking=True   
   while isAsking:
      singleword=input("Введите сюда своё слово:").lower()
      wordlist.append(singleword)
      inputAnotherWord=input("Хотите ввести ещё одно слово? (д/Н) ")
      if inputAnotherWord.capitalize()!= "Д":
         isAsking=False

def create_new_word_list_file(wordlist):
   if list.__len__(wordlist) != 0:
      with open("hangman_word_list.csv","w") as csvfile:
         for str in wordlist:
            w = csv.writer(csvfile,delimiter=",")
            templist = [str]
            w.writerow(templist)

ask_user_for_words()
create_new_word_list_file(wordlist)