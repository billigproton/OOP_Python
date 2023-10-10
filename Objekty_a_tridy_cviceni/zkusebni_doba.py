# Zkušební doba

class Employee:
    def __init__(self, name, position, holiday_entitlement, probation_period): # přidání atributu probation_period
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.probation_period = probation_period # nesmíme ho zapomenout přidat i sem
    def __str__(self): #upravení metody __str__ na zjištění, zda je zaměstnanec ještě ve zkušební době
        if self.probation_period == True:
            return f"Zaměstnanec {self.name} pracuje na pozici {self.position} a je ve zkušební době."
        else:
            return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

frantisek = Employee("František Novák", "konstruktér", 25, True)
print(frantisek)