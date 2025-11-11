s="Out of all the numbers, 10, 45, 99, and 120 were the highest marks."
import re
p=re.compile(r'\b\d{2}\b')
print(p.findall(s))