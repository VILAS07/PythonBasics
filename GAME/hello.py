# Given a string "HELLO", create a dictionary where each character maps to the list of its index positions.
#
# Example: "HELLO" → {'H':[0], 'E':[1],'L':[2,3], '0':[4]}

s="HELLO"
d={}
c=0
e=[]
l="".join(s)
# for i in l:
#     d[i]=l.index(i)
# print(d)
for i,j in enumerate(s):
    if j not in d:
        d[j]=[]
        d[j]=[i]
    else:
        d[j].append(i)
print(d)


