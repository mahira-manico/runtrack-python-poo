class Form:
    #Base class for geometric shapes
    def Aire(self):
        #Default method
        return 0

class Rectangle(Form):
    #Rectangle class inheriting from Form
    def __init__(self,length,width):
        #Initialize length and width
        self.length=length
        self.width=width

    def Aire(self):
        #Calculate and return the area
        a=self.length*self.width
        return a

#Instance creation and testing
rec=Rectangle(10,50)
print(rec.Aire())