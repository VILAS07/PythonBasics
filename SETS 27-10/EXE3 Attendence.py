m= {'John', 'Alice', 'Bob', 'Rachel', 'Steve'}
w={'Alice','Bob', 'Rachel', 'David', 'Emma'}
print(m.intersection(w))
print(m.difference(w))
print(w.difference(m))
print(f" At Least one day Students : {m.union(w)}")
print(m.symmetric_difference(w))