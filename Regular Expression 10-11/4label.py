s=" The labels 5, 7abc, and 9_hello were printed correctly"
import re
pat=re.compile(r'\b\d\w*\b')
print(pat.findall(s))