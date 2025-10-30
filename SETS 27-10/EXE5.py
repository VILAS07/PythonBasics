x= {'John', 'Alice', 'Bob', 'Rachel', 'Steve'}
y= {'Rachel', 'Steve', 'David', 'Emma', 'Bob'}
print(x.intersection(y))
print(x.difference(y))
print(y.difference(x))
print(f"Both Sections : {x.union(y)}")
print(x.symmetric_difference(y))