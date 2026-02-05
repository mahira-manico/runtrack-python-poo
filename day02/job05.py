class Car:
    def __init__(self,brand,model,year,mileage):
        self.__brand=brand
        self.__model=model
        self.__year=year
        self.__mileage=mileage
        self.__is_running=False
        self.__tank=50
    
    def __str__(self):
        return f"The car {self.__brand} is a {self.__model} from {self.__year} with a mileage at {self.__mileage}. She is currently {self.start()} with a fuel at {self.__verify_full}"
    
    def get_brand(self):
        return self.__brand
    def set_brand(self,new_brand):
        self.__brand=new_brand
    def get_model(self):
        return self.__model
    def set_model(self, new_model):
        self.__model=new_model
    def get_year(self):
        return self.__year
    def set_year(self, new_year):
        self.__year=new_year
    def get_mileage(self):
        return self.__mileage
    def set_mileage(self,new_mileage):
        self.__mileage=new_mileage
    def get_running(self):
        return self.__is_running
    def get_tank(self):
        return self.__tank
    def set_tank(self, new_tank):
        self.__tank=new_tank

    def start(self):
        if self.__is_running==False and self.__verify_full()>=5:
            self.__is_running=True
            print("Car is running")
        else:
            print("error, tank fuel must be above 5")

    def stop(self):
        if self.__is_running==True:
            self.__is_running=False
            print("Car is stopping")
        else:
            print("No car currently running")
    
    def __verify_full(self):
        return self.get_tank()
        

Mercedes=Car("Mercedes","Benz","2005",1500)
Mercedes.set_tank(-50)
Mercedes.start()
Mercedes.stop()
Mercedes.set_tank(60)
Mercedes.start()
Mercedes.stop()


    

