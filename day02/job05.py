class Car:
    def __init__(self,brand,model,year,mileage):
        self.__brand=brand # Brand name
        self.__model=model # Car model
        self.__year=year # Production year
        self.__mileage=mileage # Distance traveled
        self.__is_running=False # Engine status
        self.__tank=50 # Fuel amount
   
    def __str__(self):
        # Return car info as string
        return f"Car: {self.__brand} {self.__model} ({self.__year}). Mileage: {self.__mileage}. Fuel: {self.__tank}L"
  
    #Initializing of setters and getters
    def get_brand(self): return self.__brand
    def set_brand(self,new_brand): self.__brand=new_brand
    def get_model(self): return self.__model
    def set_model(self,new_model): self.__model=new_model
    def get_year(self): return self.__year
    def set_year(self,new_year): self.__year=new_year
    def get_mileage(self): return self.__mileage
    def set_mileage(self,new_mileage): self.__mileage=new_mileage
    def get_running(self): return self.__is_running
    def get_tank(self): return self.__tank
    def set_tank(self,new_tank): self.__tank=new_tank # Change fuel level
    
    def start(self): 
        # Start only if stopped and has enough fuel
        if self.__is_running==False and self.__verify_full()>=5:
            self.__is_running=True
            print("Car is running")
        else:
            print("Error: fuel must be at min 5L or car is already running!")
  
    def stop(self):
        # Stop only if car is running
        if self.__is_running==True:
            self.__is_running=False
            print("Car is stopping")
        else:
            print("No car currently running")

    def __verify_full(self):
        # Private method to check fuel level
        return self.get_tank()
    
# Testing the car
Mercedes=Car("Mercedes","Benz","2005",1500)
Mercedes.set_tank(0) # Empty the tank
Mercedes.start() # Should fail
Mercedes.set_tank(60) # Fill the tank
Mercedes.start() # Should work
Mercedes.stop()