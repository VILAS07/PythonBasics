name=input('enter the file name')
if name.endswith(".pdf"):
    print("PDF File")
elif name.endswith(".csv"):
    print("CSV file")
else:
    print('Unknown File Type')