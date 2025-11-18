class Mobile:
    def __init__(self,Brand,Model,Storage,Price):
        self.brand=Brand
        self.model=Model
        self.storage=Storage
        self.price=Price

    def display_info(self):
        print(f'Brand : {self.brand}')
        print(f'Model : {self.model}')
        print(f'Storage : {self.storage} GB')
        print(f'Price : {self.price} INR')

    def upgrade_storage(self,new_storage):
        self.storage+=new_storage
        print(f'Your Storage Upgraded Successfully Total : {self.storage}GB')

    def Apply_Discount(self,percentage):
        print(f'Your Discounted price is {self.price-(self.price*(percentage/100))}')

ph1=Mobile('Realme','Realme 8',128,16000)
ph2=Mobile('Iphone','17 Pro Max',1024,150000)
ph1.display_info()
ph1.upgrade_storage(128)
ph1.Apply_Discount(30)
print()
ph2.display_info()
ph2.upgrade_storage(128)
ph2.Apply_Discount(30)