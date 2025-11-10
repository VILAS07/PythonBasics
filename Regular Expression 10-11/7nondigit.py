s="The message hello and world! are fine, but abc123 and 3cats are not."
import re
p=re.compile(r'\b[a-zA-Z]+\b')
print(p.findall(s))