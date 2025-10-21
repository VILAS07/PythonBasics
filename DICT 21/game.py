menu = {"coffee", "tea", "sandwich", "juice", "cake"}
total=0
print("Welcome to Café Python ☕\nMenu: coffee, tea, sandwich, juice, cake")
while True:
    a=input('Enter your Order : ')
    if a=='coffee':
        total+=15
    elif a=='tea':
        total+=15
    elif a=='sandwich':
        total+=45
    elif a=='juice':
        total+=20
    elif a=='cake':
        total+=100
    elif a=='done':
        break
print("price : ",total)
if total>=200:
    t=total-(total*0.1)
    print(f"Bill After Discound : {t}")
    print('Thank you for visiting Café Python!')
