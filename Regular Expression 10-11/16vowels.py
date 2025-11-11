s="The cooperation between the teams was so smooth and beautiful to watch."
import re
p=re.compile(r'\b[a-zA-Z]*[aeiouAEIOU]{3,}[a-zA-Z]*\b')
print(p.findall(s))