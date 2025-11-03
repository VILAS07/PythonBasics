d=["cat", "elephant", "dog", "rabbit", "tiger"]
res=list(filter(lambda a:len(str(a))>4,d))
print(res)