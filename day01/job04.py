class Person:
    def __init__(self, surname,name):
        self.surname=surname
        self.name=name
    
    #creation of introduction method that return a string
    def ToIntroduce(self):
        return f"I am {self.name} {self.surname}"

#Creation of two instances
person1=Person("Doe", "John")
person2=Person("Dupond", "Jean")

#using of ToIntroduce method
introduction1=person1.ToIntroduce()
introduction2=person2.ToIntroduce()

#Display of the two introduction
print(f"{introduction1}\n{introduction2}")