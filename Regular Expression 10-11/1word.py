s="I like to eat apple, banana, and sunshine fruits during summer"
import re
pat=re.compile(r'\b[a-zA-Z]{5,}\b')
print(pat.findall(s))