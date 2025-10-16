l = ["Inception", "Titanic", "Avatar", "Interstellar", "Joker"]

m=input('enter the movie name')
l.append(m)
r=input('enter the movie you dont like')
l.remove(r)
z=len(l)//2
x=input('enter a new movie name')
l.insert(z,x)
print(l)


