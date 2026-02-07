class BankAccount:
    #Class managing bank accounts with private attributes
    def __init__(self,bankID,name,surname,balance):
        #Private attributes for security
        self.__bankID=bankID
        self.__name=name
        self.__surname=surname
        self.__balance=balance
        self.__overdraft=True
        self.__agios=0.5
    
    def get_balance(self):
        #Return current balance
        return self.__balance
    def set_balance(self, new_balance):
        #Update balance value
       self.__balance=new_balance
    
    def display(self):
        #Show full account details
        print("--Bank Account--\n")
        print(f"--Client ID: {self.__bankID}")
        print(f"--Name: {self.__name}")
        print(f"--Surname: {self.__surname}")
        print(f"--Balance: {self.__balance}$")
    
    def display_balance(self):
        #Show only current balance
        print(f"--Balance: {self.get_balance()}$")

    def payement(self,payement):
        #Deposit money into account
        self.__balance+=payement
        print(f"A payement of {payement}$ have been sent to your account")

    def withdrawal(self,withdrawal):
        #Logic for withdrawing money considering overdraft
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
        #Apply fees if account is in overdraft
       if self.__balance<=0 and self.__overdraft==True:
          self.__balance-=self.__agios
          print(f"Agios applied. Your current funds: {self.get_balance()}")
       else:
          print("nothing to apply, you're not on overdraft")
    
    def transfer(self,reference, amount):
        #Transfer money between two bank account objects
       if self.__balance>=amount:
          self.__balance-=amount
          other_balance=reference.get_balance()
          reference.set_balance(other_balance+amount)
          print(f"Transfer of {amount}$ successful")
       else:
          print("Not enough money!")

#Testing bank operations
Patty=BankAccount(125,"Patty","Mullhouse",10000)
Patty.display()
Patty.payement(5000)
Patty.display()
Patty.agios()

Martin=BankAccount(50, "Martin", "Mullhouse", -10)
Patty.transfer(Martin,10)
Martin.display()


