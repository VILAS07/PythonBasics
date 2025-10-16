p=input("enter plan type data/voice/combo")
if p=="data":
    print("199 for 1.5GB/day")
elif p=="voice":
    print('149 for unlimited calls')
elif p== "combo":
    v=input('enter the validity 28/56')
    if v=="28":
        print('price = 399')
    elif v=="56":
        print('price = 699')
else:
    print("Invalid plan")
