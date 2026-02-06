class Vehicle:
    def __init__(self,brand,model,year,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price

    def vehicleInformations(self):
        print("--vehicle informations--")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}$")
    
class Car(Vehicle):
    def __init__(self,brand,model,year,price):
        super().__init__(brand,model,year,price)
        self.doors=4
    
    def vehicleInformations(self):
        super().vehicleInformations()
        print(f"Doors: {self.doors}")

class Moto(Vehicle):
    def __init__(self,brand,model,year,price):
        super().__init__(brand,model,year,price)
        self.wheels=2
    
    def vehicleInformations(self):
        super().vehicleInformations()
        print(f"Wheels: {self.wheels}")
    

car=Car("Mercedes","Benz",2003,15000)
car.vehicleInformations()
moto=Moto("Harley Davidson","1200 Vmax",2025,500000)
moto.vehicleInformations()