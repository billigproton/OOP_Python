# Balík

class Package:

    def __init__(self, address, weight, state): 
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):

        print(f"Balík na adresu {self.address} má hmotnost {self.weight} kg, je ve stavu {self.state}")

balik_1 = Package("Štupartská 15", 10.0, "nedoručen")
balik_2 = Package("Mělnická 12", 0.456, "doručen")

balik_1.get_info()
balik_2.get_info()
