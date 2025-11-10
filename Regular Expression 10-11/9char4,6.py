s="The words book, table, and pencil are good, but abc and teacher are not."
import re
p=re.compile(r'\b\w{4,6}\b')
print(p.findall(s))