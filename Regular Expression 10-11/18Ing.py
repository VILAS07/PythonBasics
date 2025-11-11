s="The children were singing and dancing while it started raining."
import re
p=re.compile(r'\b\w+ing\b')
print(p.findall(s))