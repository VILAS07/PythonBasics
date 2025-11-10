employees = [
    {"name": "John", "salary": 45000},
    {"name": "Alice", "salary": 52000},
    {"name": "Bob", "salary": 60000},
    {"name": "Daisy", "salary": 48000}
]
l=list(filter(lambda a:a['salary']>50000,employees))
print(l)