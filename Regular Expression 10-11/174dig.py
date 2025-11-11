s="The invoice IDs are 9087, 123456, and 45 for three separate orders."
import re
p=re.compile(r'\b\d{4,}\b')
print(p.findall(s))