import math
class Form:
    def Aire(self):
        return 0

class Rectangle(Form):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def Aire(self):
        a=self.length*self.width
        return f"Aire: {a}cm²"

class Circle(Form):
    def __init__(self, radius):
        self.radius=radius
    
    def Aire(self):
        a=(self.radius**2)*math.pi
        return f"Aire: {round(a,1)} cm²"

rec=Rectangle(10,20)
print(rec.Aire())

circle=Circle(20)
print(circle.Aire())