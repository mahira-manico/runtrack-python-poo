class Person:
    #Base class representing a person
    def __init__(self):
        #Default age initialization
        self.age=14
    
    def display_age(self):
        #Return the current age
        return self.age   
    
    def hello(self):
        #Simple greeting message
        print("Hello")
    
    def modifyAge(self,new_age):
        #Update age with integer conversion
        self.age=int(new_age)

class Student(Person):
    #Student class inheriting from Person
    def goingToClass(self):
        #Display message
        print("i'm going to class")
    
    def displayAge(self):
        #Formatted age display using parent method
        print(f"i'am {self.display_age()} years old.")

class Professor:
    #Class representing a professor with private subject
    def __init__(self,subjectTaught):
        #Private attribute for subject
        self.__subjectTaught=subjectTaught
    
    def get_subjectTaught(self):
        #Getter for the private subject attribute
        return self.__subjectTaught
    
    def Teach(self):
        #Display professor words
        print("Class will start soon")

#Testing instances and inheritance
person1=Person()
person1.display_age()
student1=Student()
student1.displayAge()




