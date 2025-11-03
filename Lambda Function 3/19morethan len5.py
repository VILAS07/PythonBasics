data=["Tom", "Jennifer", "Chris", "Amanda", "Joe"]
l=list(filter(lambda a:len(str(a))>5,data))
print(l)