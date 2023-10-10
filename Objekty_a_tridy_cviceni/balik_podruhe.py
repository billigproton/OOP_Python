# Balík podruhé

class Package:

    def __init__(self, address, weight, state): 
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):

        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg, je ve stavu {self.state}"
    
    def deliver(self):
        if self.state == "doručen":
            print(f"Balík již byl doručen")
        
        else: 
            self.state = "doručen"
            print(f"Doručení uloženo")

balik_1 = Package("Štupartská 15", 10.0, "nedoručen")
balik_2 = Package("Mělnická 12", 0.456, "doručen")

print(balik_1)

balik_1.deliver() # Výstup: "Doručení uloženo"
balik_1.deliver() # Výstup: "Balík již byl doručen"
