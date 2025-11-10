s="Please check code1 and test5 before submitting the report."
import re
pat=re.compile(r'\b\w*\d\b')
print(pat.findall(s))