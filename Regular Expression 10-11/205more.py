s="Continuous learning helps improve knowledge and problem-solving skills."
import re
p=re.compile(r'\b\w{5,}\b')
print(p.findall(s))