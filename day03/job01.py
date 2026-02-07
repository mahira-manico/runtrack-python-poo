class City:
    #Class representing a city with private attributes
    def __init__(self,name,inhabitants):
        #Private attributes for encapsulation
        self.__name=name
        self.__inhabitants=inhabitants
    
    #Getters and setters for city attributes
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name=new_name
    
    def get_inhabitants(self):
        return self.__inhabitants
    def set_inhabitants(self, new_number):
        self.__inhabitants=new_number

    def __str__(self):
        #String representation of the city state
        return f"There is {self.get_inhabitants()} inhabitants in {self.get_name()}"


class Person:
    #Class representing a person linked to a city object
    def __init__(self,name,age,city_object):
        #Private attributes including an object reference
        self.__name=name
        self.__age=age
        self.__city_object=city_object
    
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name=new_name
    
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        self.__age=new_age
    
    def get_city_object(self):
        #Returns the city object reference
        return self.__city_object
    
    def addPerson(self,new_person):
            #Modifies the city inhabitants via object reference
            current=self.__city_object.get_inhabitants()
            self.__city_object.set_inhabitants(current+new_person)
            print(f"Population of {self.__city_object.get_name()} updated to {self.__city_object.get_inhabitants()}")
            

#Instances creation and testing
Paris=City("Paris",10000000)
Marseille=City("Marseille", 861635)

John=Person("John", 45,Paris)
John.addPerson(1)
print(Paris)

Myrtille=Person("Myrtille",4,Paris)
Myrtille.addPerson(1)
print(Paris)

Chloe=Person("Chloé",18,Marseille)
Chloe.addPerson(1)
print(Marseille)