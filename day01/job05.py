#Creation of class
class Point:
    def __init__(self,x,y): #Using of build method "__init__"
        self.x=x #Creation of variables
        self.y=y
    
    #Creation of methods
    def DisplayPoints(self): #Display x and y values
        return f"x={self.x} y={self.y}"
    
    def DisplayX(self): #Display X value only
        return f"x is {self.x}"

    def DisplayY(self): #Display Y value only
        return f"y is {self.y}"
    
    def ChangeY(self,changeY): #Change Y value
        self.y=changeY
    
    def ChangeX(self,changeX): #Change X value
        self.x=changeX

initializing=Point(10,20) #Creation of instance 

display=initializing.DisplayPoints() #Call of method to display all points

change1=initializing.ChangeX(50) #Call of method to change value

display2=initializing.DisplayPoints()

change2=initializing.ChangeY(30)

display3=initializing.DisplayPoints()

display4=initializing.DisplayY() #Call of method to display one value
 
#Display of all changes on shell
print(f" Initialization: {display}\n Change of X: {display2}\n Change of Y: {display3}\n Display of Y: {display4}")

