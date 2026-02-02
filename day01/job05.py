class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def DisplayPoints(self):
        return f"x={self.x} y={self.y}"
    
    def DisplayX(self):
        return f"x is {self.x}"

    def DisplayY(self):
        return f"y is {self.y}"
    
    def ChangeY(self,changeY):
        self.y=changeY
    
    def ChangeX(self,changeX):
        self.x=changeX

initializing=Point(10,20)

display=initializing.DisplayPoints()

change1=initializing.ChangeX(50)

display2=initializing.DisplayPoints()

change2=initializing.ChangeY(30)

display3=initializing.DisplayPoints()

display4=initializing.DisplayY()

print(f" Initialization: {display}\n Change of X: {display2}\n Change of Y: {display3}\n Display of Y: {display4}")

