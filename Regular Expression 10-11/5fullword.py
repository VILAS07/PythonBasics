s="The words apple and sky look fine, but no4you and go2 do not."
import re
pat=re.compile(r'\b[A-Za-z]+\b')
print(pat.findall(s))