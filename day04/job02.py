class Person:
    def __init__(self):
        self.age=14
    def display_age(self):
        return self.age # Returns the integer
    def hello(self):
        print("Hello") # Just print, no need to return None
    def modifyAge(self,new_age):
        self.age=int(new_age)

class Student(Person):
    def goingToClass(self):
        print("I'm going to class")
    def displayAge(self):
        # We use self.display_age() inherited from Person
        print(f"I am {self.display_age()} years old.")
    def displayHello(self):
        self.hello() # Inherited method

class Professor:
    def __init__(self,subjectTaught):
        self.__subjectTaught=subjectTaught
    def get_subject(self):
        return self.__subjectTaught
    def get_age(self,person_object):
        # Using reference to another object
        print(f"I am {person_object.display_age()} years old.")
    def get_hello(self,person_object):
        person_object.hello()
    def Teach(self):
        print("Class will start soon")

#test
person1=Person()
student1=Student()
student1.displayAge() # Output: 14
student1.displayHello() # Output: Hello

student1.modifyAge(20) # We modify student age
student1.displayAge()

prof_person=Person() # The person object for the professor
prof_person.modifyAge(40)
prof1=Professor("Algebra")
prof1.get_age(prof_person) # Output: 40 
prof1.get_hello(prof_person)
