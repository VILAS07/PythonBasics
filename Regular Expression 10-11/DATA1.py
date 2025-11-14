with open('data (2).txt','r') as file:
    a=file.read()
import re
#1
# email=re.compile(r'\b[\w.-]+@[\w.-]+\b')
# print(email.findall(a))

#2
# ph=re.compile(r'Phone: \b[0-9]\b')
# print(ph.findall(a))

#3
# ind=re.compile(r'\+?91? ?[\d]{5}[ -]?\d{5}|9\d{5}[- ?\d{5}]')
# print(ind.findall(a))

#4
# emp=re.compile(r'\bEMP-\d{4}\b')
# print(emp.findall(a))

#5
# ip=re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
# print(ip.findall(a))

#6
# user=re.compile(r'user\s+(\S+)')
# print(user.findall(a))

#7
# date=re.compile(r'\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}')
# print(date.findall(a))

#8
# employee=re.compile(r'Name:\s*(.*?)\s*\|')
# print(employee.findall(a))

#10
# time=re.compile(r'\d{2}:\d{2}:\d{2}')
# print(time.findall(a))

#11
# word=re.compile(r'')
# print(word.findall(a))

# #12
# CPWO=re.compile(r'\b[A-Z][a-zA-Z]+\b')
# print(CPWO.findall(a))

#13
year=re.compile(r'\d{2}/\d{2}/(\d{4})|(\d{4})-\d{2}-\d{2}')
print(year.findall(a))

#14
# backup=re.compile(r'Backup created on\s*(.*)')
# print(backup.findall(a))

#15
backup=re.compile(r'192\.\d|172\.\d')
print(backup.findall(a))
