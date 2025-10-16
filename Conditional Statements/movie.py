m=input('enter a movie type 2d or 3d')
if m=="2D":
    print('normal price = 150')
elif m=="3D":
    s=input("enter the seat type normal or premium")
    if s=="normal":
        print("price = 250")
    elif s=="premium":
        print("price = 350")
else:
    print("Invalid movie type")