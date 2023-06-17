import re

text= "Москва: 777, 999, 797. Тула: 071, 950, 112."
print (re.findall("\d",text))
print (re.findall("[0-9]{3}",text))