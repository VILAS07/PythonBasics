
class Movie:
    def __init__(self,Title,Genre,Ticket_Price,Seats_Available):
        self.title=Title
        self.genre=Genre
        self.ticket_price=Ticket_Price
        self.seats_avail=Seats_Available

    def display_info(self):
        print(f'Title : {self.title}')
        print(f'Genre : {self.genre}')
        print(f'Ticket Price : {self.ticket_price}')
        print(f'Seats Available : {self.seats_avail}')

    def book_ticket(self,count):
        if self.seats_avail>=count:
            self.seats_avail-=count
            print(f'{count} seats booked successfully')
        else:
            print('Not Enough seats available')
    def total_earning(self):
        a=(200-self.seats_avail)*self.ticket_price
        print(f'Total Earning : {a} Rupees')
        return a

movie1=Movie('OnePiece','Anime',500,200)
movie2=Movie('Interstellar','SciFi',1000,200)
movie1.display_info()
print()
movie1.book_ticket(7)
movie1.book_ticket(200)
movie1.total_earning()
movie1.display_info()
print()
movie2.display_info()
print()
movie2.book_ticket(10)
movie2.book_ticket(200)
movie2.total_earning()
movie2.display_info()
