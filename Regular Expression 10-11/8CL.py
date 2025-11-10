s=" Hello and World123 are correct, but hi and A are not."
import re
p=re.compile(r'\b[A-Z]\w+\b')
print(p.findall(s))