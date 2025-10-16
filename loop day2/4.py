files = ["report.pdf", "photo.jpg", "data.csv", "notes.txt", "script.py"]
for i in files:
    a=i.split('.')
    print(f"{a[0]} : {a[1]}")