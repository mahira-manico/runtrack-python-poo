import math #library import to use Pi

class Circle:
    def __init__(self,radius):
        self.radius=radius #Variable radius

    def changeRadius(self,radius): #method to change radius
        self.radius=radius
        
    def displayInfo(self): #method to display all circle informations
        print(f"radius:{self.radius},circonference:{self.circumference()},aire:{self.area()},diametre:{self.diameter()}")

    def circumference(self): #calcul circumference
        return 2*math.pi*self.radius

    def area(self): #calcul area of circle
        return math.pi*(self.radius**2)
        
    def diameter(self): #calcul diameter of circle
        return 2*self.radius

circle1=Circle(4) #Instance creation
circle1.displayInfo() #method call to display informations
circle2=Circle(7)
circle2.displayInfo()
circle2.changeRadius(10) #method to change radius without calling Circle
circle2.displayInfo()
        