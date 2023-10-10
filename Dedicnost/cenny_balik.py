# Cenný balík

class Package:

    def __init__(self, address, weight, state): 
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):

        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg, je ve stavu {self.state}."
 
class ValuablePackage(Package): # Systém lze vylepšit - např. vnořením podmínky na zjišťování, zda se jedná o klasický balík či o cenný balík na základě hodnoty balíku

    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() + f" Jedná se o cenný balík s hodnotou {self.value} Kč."
    

balik_1 = Package("Jeronýmova 14", 20, "doručen")

print(balik_1)

cenny_balik1 = ValuablePackage("Komunardů 23", 15, "doručen", 10000)

print(cenny_balik1)



