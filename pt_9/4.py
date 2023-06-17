my_list=list()
# First line is the same to that line:
#my_list=[]

with open("st.txt","r") as f:
    my_list.append(f.read())
print(my_list)