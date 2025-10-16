x=int(input("enter number 1"))
y=int(input("enter number 2"))
z=int(input("enter number 3"))
print(f"Average of {x} {y} {z} is {(x+y+z)/3}")

s=0
n=int(input("enter total  number"))
for _ in range(n):
    x = int(input("enter number 1"))
    s+=x
print(f"AVERAGE : {s/n}")
