import math
class Form:
    #Base class representing a geometric shape
    def Aire(self):
        #Method to be overridden by child classes
        return 0

class Rectangle(Form):
    #Child class for rectangle shapes
    def __init__(self,length,width):
        #Initialize dimensions
        self.length=length
        self.width=width

    def Aire(self):
        #Calculate area for rectangle
        a=self.length*self.width
        return f"Aire: {a}cm²"

class Circle(Form):
    #Child class for circular shapes
    def __init__(self, radius):
        #Initialize radius
        self.radius=radius
    
    def Aire(self):
        #Calculate area for circle using pi
        a=(self.radius**2)*math.pi
        return f"Aire: {round(a,1)} cm²"

#Instance creation and area calculation
rec=Rectangle(10,20)
print(rec.Aire())

circle=Circle(20)
print(circle.Aire())