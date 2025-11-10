import re
s='9746906494 1234567890123456 gini12@gmail.com hari@yahoo.com'
ph=re.compile(r'\b\d{10}\b')
print(ph.findall(s))
# gm=re.compile(r'[a-zA-Z0-9]+')
# print(gm.findall(s))