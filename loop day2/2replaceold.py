ads = ["Welcome to SmartTech", "SmartTech launches new product", "SmartTech is hiring!"]
for i in ads:

    for j in range(len(i)):
        if ads[j]=='SmartTech':
            ads[j]='TechSmart'
print(ads)