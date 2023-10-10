# Kniha podruhé

class Book:
    def __init__(self, title, pages, price, sold, costs): # přidání atributu costs
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs # nesmím zapomenout ho dát i zde

    def get_info(self):
        print(f"Kniha {self.title} má {self.pages} stránek a stojí {self.price} Kč")
    
    def get_time_to_read(self):
        potrebny_cas = self.pages / 4

        return f"Kniha {self.title} ti zabere cca {potrebny_cas} minut než ji přečteš"
    
    def profit(self): # metoda profit
        self.sold * (self.price - self.costs)
        return f"Profit je {self.sold * (self.price - self.costs)} Kč"

    def rating(self): # metoda rating
        if self.sold * (self.price - self.costs) < 50000:
            print(f"Tahle kniha je propadák")
        
        elif self.sold * (self.price - self.costs) > 50000 and self.sold * (self.price - self.costs) < 500000:
            print(f"Tahle kniha je průměr")

        else: 
            print(f"Tahle kniha je úspěch")

    
kniha_1 = Book("Babička", 360, 299, 125838, 100)

kniha_1.get_info()
print(kniha_1.get_time_to_read())
# volání metody profit a rating
print(kniha_1.profit())
kniha_1.rating()