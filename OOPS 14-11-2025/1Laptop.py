class Laptop:
    def __init__(self,brand,processer,ram_size,price):
        self.brand=brand
        self.processer=processer
        self.ram=ram_size
        self.price=price
    def Display_Info(self):
        print(f'Brand : {self.brand}')
        print(f'Processer : {self.processer}')
        print(f'Ram Size : {self.ram}')
        print(f'Price : {self.price}')
    def upgrade_ram(self,newsize):
        self.ram+=newsize
        print(f'RAM upgraded to {self.ram}')
    def Discount(self,percentage):
        a=self.price-(self.price*(percentage/100))
        print(f'Your Discounted price is {a}')

ob1=Laptop('Acer','I7',16,100000)
ob1.Display_Info()
ob1.upgrade_ram(8)
ob1.Discount(10)
ob1.Display_Info()
print()
ob2=Laptop('Asus','I7',16,110000)
ob2.Display_Info()
ob2.upgrade_ram(16)
ob2.Discount(20)
ob2.Display_Info()


