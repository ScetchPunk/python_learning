tv=["Breaking Bad","X-files","Fargo"]
i = 0
for show in tv:
    new=tv[i]
    new=new.upper()
    tv[i]=new
    i += 1
print(tv)
