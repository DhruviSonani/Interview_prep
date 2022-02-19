import re
def removeOccurrences(s: str, part: str) -> str:
    while part in s:
        s = re.sub(part, '', s, 1)
    return s 

s, part = "axxxxyyyyb", "xy"
print(removeOccurrences(s, part))