class BankAccount:
    def __init__(self,bankID,name,surname,balance):
        self.__bankID=bankID
        self.__name=name
        self.__surname=surname
        self.__balance=balance
        self.__overdraft=True
        self.__agios=0.5
    
    def get_balance(self):
        return self.__balance
    def set_balance(self, new_balance):
       self.__balance=new_balance
    
    def display(self):
        print("--Bank Account--\n")
        print(f"--Client ID: {self.__bankID}")
        print(f"--Name: {self.__name}")
        print(f"--Surname: {self.__surname}")
        print(f"--Balance: {self.__balance}$")
    
    def display_balance(self):
        print(f"--Balance: {self.get_balance()}$")

    def payement(self,payement):
        self.__balance+=payement
        print(f"A payement of {payement}$ have been sent to your account")

   
    def withdrawal(self,withdrawal):
      if self.get_balance()>=withdrawal and self.__overdraft==True:
        self.__balance-=withdrawal
        print(f"New balance: {self.get_balance()}")

      elif self.__balance<0 and self.__overdraft==False:
       print("you're on overdraft!")

      elif self.__balance<=withdrawal and self.__overdraft==True:
         self.__balance-=withdrawal
         print(f"New balance: {self.get_balance()}")

      else:
        print("Error! your funds are insufficient")
    
    def agios(self):
       if self.__balance<=0 and self.__overdraft==True:
          self.__balance-=self.__agios
          print(f"Agios applied. Your current funds: {self.get_balance()}")
       else:
          print("nothing to apply, you're not on overdraft")
    
    def transfer(self,reference, amount):
       if self.__balance>=amount:
          self.__balance-=amount
          other_balance=reference.get_balance()
          reference.set_balance(other_balance+amount)
          print(f"Transfer of {amount}$ to {reference.__name} successful")
       else:
          print("Not enough money!")

          
       
Patty=BankAccount(125,"Patty","Mullhouse",10000)
Patty.display()
Patty.payement(5000)
Patty.display()
Patty.agios()

Martin=BankAccount(50, "Martin", "Mullhouse", -10)
Patty.transfer(Martin,10)
Martin.display()



