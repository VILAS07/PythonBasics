s="The tent was tight, but that didn’t stop them from trying to fix it"
import re
p=re.compile(r'\bt[a-z]*t+\b')
print(p.findall(s))