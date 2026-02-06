class Form:
    def Aire(self):
        return 0

class Rectangle(Form):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def Aire(self):
        a=self.length*self.width
        return a

rec=Rectangle(10,50)
print(rec.Aire())