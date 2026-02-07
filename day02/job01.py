class Rectangle:
    def __init__(self,length,width):
        self.__length=length #private attribut
        self.__width=width

    def get_length(self): #getter
        return self.__length
    
    def set_length(self,new_length): #mutter
        self.__length=new_length

    def get_width(self): #getter
        return self.__width
    
    def set_width(self, new_width): #mutter
        self.__width=new_width

rectangle=Rectangle(10,5) #set instance

print(rectangle.get_length()) #display length
rectangle.set_length(6) #change length
print(rectangle.get_length())
rectangle.set_width(20) #change width
print(rectangle.get_width())
