s="The house number is 1234, and the pin code nearby is 560098."
import re
p=re.compile(r'\b[a-zA-Z]{4}\b')
print(p.findall(s))