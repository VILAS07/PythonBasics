countries = {
    "India": "New Delhi",
    "France": "Paris",
    "Japan": "Tokyo",
    "Australia": "Canberra"
}
print(countries)
for i,j in countries.items():
    if i=='France':
        countries.pop(i)
        break
print(countries)