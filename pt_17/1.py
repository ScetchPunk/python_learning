import re

l = "Красивое лучше, чем уродливое."
matches = re.findall("Красивое", l)

print(matches)