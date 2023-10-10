# Jízdenky a letenky

class BusTicket:
    def __init__(self, basic_price, seat_number):
        self.basic_price = basic_price
        self.seat_number = seat_number

class TrainTicket(BusTicket):
    def __init__(self, basic_price, seat_number, fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class

    def get_price(self):
        if self.fare_class == "economy":
            return f"Cena vlakové jízdenky je {self.basic_price} Kč."
        elif self.fare_class == "business":
            return f"Cena vlakové jízdenky je {self.basic_price * 1.2} Kč."
        

class PlaneTicket(TrainTicket):
    def __init__(self, basic_price, seat_number, fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages

    def get_price(self):
        luggage_price = self.checkout_luggages * 2000
        if self.fare_class == "economy":
            return f"Cena letenky je {self.basic_price + luggage_price} Kč."
        elif self.fare_class == "business":
            return f"Cena letenky je {self.basic_price * 1.5 + luggage_price} Kč."
        
train_ticket1 = TrainTicket(150, 13, "economy")
train_ticket2 = TrainTicket(150, 13, "business")

print(train_ticket1.get_price())
print(train_ticket2.get_price())

plane_ticket1 = PlaneTicket(6000, 12, "economy", 1)
plane_ticket2 = PlaneTicket(6000, 12, "business", 1)

print(plane_ticket1.get_price())
print(plane_ticket2.get_price())