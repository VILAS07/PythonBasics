s="The users admin, root, and support123 have access to the main server."
import re
p=re.compile(r'\b[^\d]+\b')
print(p.findall(s))