class Car:
    def __init__(self,Brand,Model,Year,Price):
        self.Brand=Brand
        self.Model=Model
        self.Year=Year
        self.Price=Price

    def Start(self):
        print(f'The {self.Brand} {self.Model} is Starting')

    def Display_info(self):
        print('BRAND : ',self.Brand)
        print('Model : ',self.Model)
        print('Year : ',self.Year)
        print('Price : ',self.Price)

    def age_of_car(self):
        print(f'Age of car : {2025 - self.Year} Years')

    def discounted_price(self,DP):
        print(f'Price after {int(DP*100)} discount: ₹{self.Price-(self.Price*DP)}')

car1=Car('Toyota','Corolla',2018,1500000)
car2=Car('Ford','Mustang',2020,5500000)
print()
car1.Start()
car1.Display_info()
car1.age_of_car()
car1.discounted_price(0.1)
print()
car2.Start()
car2.Display_info()
car2.age_of_car()
car2.discounted_price(0.05)
