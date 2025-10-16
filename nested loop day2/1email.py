emails = ["john@gmail.com", "mia@yahoo.com", "arun@outlook.com"]
s=''
j=''
for i in emails:
    n,d=i.split('@')
    print(n,"-->",d)