class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.name=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} added Successfully")

    def WithDraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"{amount} Withdrawn Successfully")
        else:
            print('Insufficient Balance')

    def Display_Balance(self):
        print(f'Balance : {self.balance}')

a=BankAccount('Vilas')
a.Display_Balance()
a.deposit(1000)
a.Display_Balance()
a.WithDraw(10000)
a.Display_Balance()