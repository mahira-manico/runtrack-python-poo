class Person:
    def __init__(self):
        self.age=14
    
    def display_age(self):
        return self.age   
    
    def hello(self):
        return "Hello"
    
    def modifyAge(self,new_age):
        self.age=int(new_age)

class Student(Person):

    def goingToClass(self):
        return "i'm going to class"
    
    def displayAge(self,person_object):
        print(f"i'am {person_object.display_age()} years old.")

class Professor:
    def __init__(self,subjectTaught):
        self.__subjectTaught=subjectTaught
    
    def get_subjectTaught(self):
        return self.__subjectTaught
    
    def Teach(self):
        print("Class will start soon")

person1=Person()
person1.display_age()
student1=Student()
student1.displayAge(person1)





