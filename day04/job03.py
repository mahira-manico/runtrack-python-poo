class Rectangle:
    #Base class with private attributes
    def __init__(self,width,length):
        #Private attributes
        self.__width=width
        self.__length=length
    
    #Getters and setters for encapsulation
    def get_width(self): return self.__width
    def set_width(self,new_width): self.__width=new_width
    def get_length(self): return self.__length
    def set_length(self,new_length): self.__length=new_length
    
    def perimeter(self):
        #Calculation using getter methods
        p=(self.get_width()+self.get_length())*2
        print(f"Perimeter: {p}cm")
        return p
    
    def surface(self):
        #Calculation of area
        s=self.get_length()*self.get_width()
        print(f"Surface: {s}cm²")
        return s

class Parallelepiped(Rectangle):
    #Derived class 
    def __init__(self,width,length,height):
     #Call parent constructor
     super().__init__(width,length)
     self.height=height
    
    def volume(self):
        #Volume calculation using inherited surface method
        v=self.surface()*self.height
        print(f"Volume: {v}cm³")
        return v

#Testing objects and inheritance
rectangle=Rectangle(10,20)
rectangle.perimeter()
rectangle.surface()
p1=Parallelepiped(10,20,30)
p1.volume()
p1.perimeter() #Inherited method
p1.surface() #Inherited method

