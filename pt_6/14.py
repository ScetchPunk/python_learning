some_text="    Беларусь       "
s=some_text.strip()
print(s)
some_text="Sabaton"
print(some_text.replace("a","@"))
some_text="Sabaton"
try:
    print(some_text.index("f"))
except ValueError:
    print("Символа не найдено!")
print(some_text.index("a"))
