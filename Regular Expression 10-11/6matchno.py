s="You can contact me at 9876543210 or 9998887776 for details."
import re
p=re.compile(r'\b\d{10}\b')
print(p.findall(s))