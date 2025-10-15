n=int(input("enter your age"))
if n>12:
    print("ticket = 100")
elif n>12 or n<60:
    s=input(("Are you a student"))
    if s=="yes":
        print("Ticket = 120")
    else:
        print('ticket = 150')
else:
    print('Ticket = 120')