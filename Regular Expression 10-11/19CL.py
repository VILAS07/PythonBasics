s="Riya and Sam went to Delhi last month to meet Mr. Arjun."
import re
p=re.compile(r'\b[A-Z][a-z]+\b')
print(p.findall(s))