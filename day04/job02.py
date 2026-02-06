class Person:
    def __init__(self):
        self.age=14
    
    def display_age(self):
        return self.age   
    
    def hello(self):
        hello=print("Hello")
        return hello
    
    def modifyAge(self,new_age):
        self.age=int(new_age)

class Student(Person):

    def goingToClass(self):
        print("i'm going to class")
    
    def displayAge(self,person_object):
        print(f"i'am {person_object.display_age()} years old.")
    
    def displayHello(self,person_object):
        return person_object.hello()
    

class Professor:
    def __init__(self,subjectTaught):
        self.__subjectTaught=subjectTaught
    
    def get_age(self, person_object):
        print(f"i'am {person_object.display_age()} years old.")
    
    def get_hello(seld, person_object):
        return person_object.hello()

    
    def get_subjectTaught(self):
        return self.__subjectTaught
    
    def Teach(self):
        print("Class will start soon")

person1=Person()
person1.display_age()
student1=Student()
student1.displayAge(person1)
student1.displayHello(person1)
student1.goingToClass()
person1.modifyAge(15)
student1.displayAge(person1)
prof=Person()
prof.modifyAge(40)
prof1=Professor("Algebra")
prof1.get_age(prof)
prof1.get_hello(prof)
prof1.Teach()

