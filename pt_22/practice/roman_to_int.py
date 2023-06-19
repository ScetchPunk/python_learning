def roman_to_int(s):
    result = 0
    indexer=0
    for i in range(len(s)):
        if indexer >= len(s):
            break
        if s[indexer] == "I":
            if indexer + 1 < len(s):
                if s[indexer + 1] == "V":
                    result += 4
                    indexer+=2
                    continue
                if s[indexer + 1] == "X":
                    result += 9
                    indexer+=2
                    continue
            result+=1
        if s[indexer]=="V":
            result+=5
        if s[indexer]=="X":
            if indexer + 1 < len(s):
                if s[indexer + 1] == "L":
                    result += 40
                    indexer+=2
                    continue
                if s[indexer + 1] == "C":
                    result += 90
                    indexer+=2
                    continue
            result+=10
        if s[indexer]=="L":
            result+=50
        if s[indexer]=="C":
            if indexer + 1 < len(s):
                if s[indexer + 1] == "D":
                    result += 400
                    indexer+=2
                    continue
                if s[indexer + 1] == "M":
                    result += 900
                    indexer+=2
                    continue
            result+=100
        if s[indexer]=="D":
            result+=500
        if s[indexer]=="M":
            result+=1000
        indexer+=1
    return result


print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCDLXXVI"))
