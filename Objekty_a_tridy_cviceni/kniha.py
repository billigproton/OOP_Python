# Kniha

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        print(f"Kniha {self.title} má {self.pages} stránek a stojí {self.price} Kč")
    
    def get_time_to_read(self):
        potrebny_cas = self.pages / 4

        return f"Kniha {self.title} ti zabere cca {potrebny_cas} minut než ji přečteš"
    
kniha_1 = Book("Babička", 360, 299)

kniha_1.get_info()
print(kniha_1.get_time_to_read())