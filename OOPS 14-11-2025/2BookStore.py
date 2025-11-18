class Book:
    def __init__(self,Title,Author,Price,Stock):
        self.title=Title
        self.author=Author
        self.price=Price
        self.stock=Stock
    def Display_Details(self):
        print(f'Title : {self.title}')
        print(f'Author : {self.author}')
        print(f'Price : {self.price}')
        print(f'Stock : {self.stock}')

    def Purchase(self,quantity):
        if self.stock>=quantity:
            self.stock-=quantity
            print(f'Purchased {quantity} Books')
        else:
            print('Not Enough Stock')
    def Apply_Discount(self,percentage):
        print(f'Your Discounted price is {self.price-(self.price*(percentage/100))}')

b1=Book('The Alchemist','Paulo Coelho',300,5)
b2=Book('Life of PI','Yann Martle',500,2)
b1.Display_Details()
b1.Purchase(4)
b1.Apply_Discount(10)
print()
b2.Display_Details()
b2.Purchase(3)
b2.Apply_Discount(50)
