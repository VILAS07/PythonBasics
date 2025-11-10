s="The numbers 123, 4567, and 89 were written on the board."
import re
pat=re.compile(r'\b\d{3}\b')
print(pat.findall(s))