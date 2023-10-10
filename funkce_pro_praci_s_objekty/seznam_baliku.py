# seznam balíků

class Package:

    def __init__(self, address, weight, state): 
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):

        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg, je ve stavu {self.state}."
    
    def get_costs(self):
        cena_prepravy = 0
        if self.weight <= 2:
            cena_prepravy = 150
        elif self.weight > 2 and self.weight <= 5:
            cena_prepravy = 190
        else: 
            cena_prepravy = 220
        
        return cena_prepravy

 
class ValuablePackage(Package): 

    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() + f" Jedná se o cenný balík s hodnotou {self.value} Kč."
    
    def get_costs(self):
        price = super().get_costs()
        return price * 1.05
    

balik_1 = Package("Jeronýmova 14", 20, "doručen")

print(balik_1)

cenny_balik1 = ValuablePackage("Komunardů 23", 15, "doručen", 10000)

print(cenny_balik1)

print(balik_1.get_costs())
print(cenny_balik1.get_costs())

package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]

# VYPOČTENÍ  HODNOTY BALÍKŮ V AUTĚ (ÚKOL - SEZNAM BALÍKŮ)
total_value = 0

for package in package_list:
    if hasattr(package, 'value'):
        total_value += package.value

print(f"Celková hodnota balíků v autě je {total_value} Kč.")