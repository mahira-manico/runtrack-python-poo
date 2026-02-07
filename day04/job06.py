class Vehicle:
    #Base class representing a general vehicle
    def __init__(self,brand,model,year,price):
        #Initialize common vehicle attributes
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price

    def vehicleInformations(self):
        #Display generic vehicle data
        print("--vehicle informations--")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}$")
    
    def start(self):
        #Default driving message
        print("Warning: I'm driving")
    
class Car(Vehicle):
    #Child class specializing in cars
    def __init__(self,brand,model,year,price):
        #Inherit attributes from Vehicle
        super().__init__(brand,model,year,price)
        self.doors=4
    
    def vehicleInformations(self):
        #Call parent method and add specific car info
        super().vehicleInformations()
        print(f"Doors: {self.doors}")
    
    def start(self):
        #Specific message for cars
        print("My car is driving")

class Moto(Vehicle):
    #Child class specializing in motorcycles
    def __init__(self,brand,model,year,price):
        #Inherit attributes from Vehicle
        super().__init__(brand,model,year,price)
        self.wheels=2
    
    def vehicleInformations(self):
        #Call parent method and add specific moto info
        super().vehicleInformations()
        print(f"Wheels: {self.wheels}")
    
    def start(self):
        #Specific message for motorcycles
        print("My moto is driving")
    

#Instance creation and method calls
car=Car("Mercedes","Benz",2003,15000)
car.vehicleInformations()
moto=Moto("Harley Davidson","1200 Vmax",2025,500000)
moto.vehicleInformations()
moto.start()