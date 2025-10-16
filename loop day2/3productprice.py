products = ["apple:50", "banana:20", "chocolate:100"]
for i in products:
    a=i.split(':')
    print(f"Product : {a[0]},Price : {a[1]}")