data=[("John", 17), ("Alice", 21), ("Bob", 19), ("Daisy", 16)]
l=list(filter(lambda a:a[1]>18,data))
print(l)