#creation of a class
class Operation:
    #build method with "init"
    def __init__(self,number1,number2): #add of attribute
        self.number1=number1
        self.number2=number2

#instance creation
my_number=Operation(1,2)

#print doesn't print since str build isn't initalized
print(my_number)