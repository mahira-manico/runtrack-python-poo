class Operation:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    
    def __str__(self):
        return f"Number1 is {self.number1}\nnumber2 is {self.number2}"
    
    #creation of first method to addition two values
    def addition(self):
       return self.number1+self.number2

#Initialization of the two numbers, keep it in a variable
my_number=Operation(10,20)

#creation of a new variable to stock result, call of method using "." and "()"
my_calcul=my_number.addition()

#display result 
print(my_calcul)