class Students:
    def __init__(self,name,surname,student_id,credits=0,):
        self.__name=name #Student first name
        self.__surname=surname #Student last name
        self.__student_id=student_id #Unique ID number
        self.__credits=credits #Starting credits
        self.__level=self.__studentEval() #Calculate level at start
   
    def __str__(self):
       return f"The student {self.__name} {self.__surname} have the student ID: {self.__student_id} and {self.__credits} credits points"
    
    #initializing of setters and getters
    def get_name(self):
       return self.__name
    def set_name(self,new_name):
       self.__name=new_name
    def get_surname(self):
       return self.__surname
    def set_surname(self,new_surname):
       self.__surname=new_surname
    def get_student_id(self):
       return self.__student_id
    def get_credit(self):
       return self.__credits
  
    def add_credits(self,new_credit):
        #Check if credits are positive
        if new_credit<0:
            print("error! must be superior to zero!")
        else: 
          self.__credits+=new_credit #Update total credits
          self.__level=self.__studentEval() #Update level after adding credits
          print(f"The total of credit of {self.__name} {self.__surname} is: {self.__credits} points.")
          return self.__credits
   
    def __studentEval(self):
       #Private method to decide student level
       if self.__credits>=90:
          return f"Level: Excellent"
       elif self.__credits>=80:
          return f"Level: Very Good"
       elif self.__credits>=70:
          return f"Level: Good"
       elif self.__credits>=60:
          return f"Level: Acceptable"
       else:
          return f"Level: Insufficient"
  
    def studentInfo(self):
       #Print all student details
       print(f"Nom={self.get_name()}\nSurname={self.get_surname()}\nid={self.get_student_id()}\n{self.__level}")

student1=Students("John","Doe",145)
student1.add_credits(50)
student1.add_credits(10)
student1.add_credits(5)
student1.studentInfo()


