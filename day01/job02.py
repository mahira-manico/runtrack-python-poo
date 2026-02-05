class Operation:
    def __init__(self, number1,number2):
        self.number1=number1
        self.number2=number2
    
    #creation of str build method witch allow to print result to terminal
    def __str__(self):
        return f"Number1 is {self.number1}\nNumber2 is {self.number2}"

my_number=Operation(10,2)
print(my_number)
