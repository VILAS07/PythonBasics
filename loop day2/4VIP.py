customers = ["Arya", "John", "Meera", "Alex"]
vip_list = ["John", "Alex"]
for i in customers:
    if i in vip_list:
        print(f" VIP {i}")
    else:
        print(f" Regular {i}")