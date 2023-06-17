import re

text="Привидение прошуршало и и исчезло в углу."
print(text)
print(re.findall(".ло",text,re.IGNORECASE))