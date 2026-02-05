from enum import Enum

class Status(Enum):
    IN_PROGRESS="In progress"
    FINISHED="Finished"
    CANCELED="Canceled"


class Command:
    def __init__(self,idOrder):
        self.__idOrder=idOrder
        self.__ordered_dishes={}
        self.__order_statut=Status.IN_PROGRESS
        self.__vat=20
    
    def get_idOrder(self):
        return self.__idOrder    
    def set_idOrder(self, new_order):
        self.__idOrder=new_order
    
    def get_ordered_dishes(self):
        return self.__ordered_dishes
    def set_ordered_dishes(self, new_ordered_dishes):
        self.__ordered_dishes=new_ordered_dishes
    
    def get_order_statut(self):
        return self.__order_statut
    
    def get_vat(self):
        return self.__vat
    
    def add_dish(self,new_dish,price):
        if self.get_order_statut()==Status.IN_PROGRESS:
         self.get_ordered_dishes()[new_dish]=price
         print(f"{new_dish} at {price}$ added to order")
    
    def cancel_order(self):
        self.__order_statut=Status.CANCELED
        self.get_ordered_dishes().clear()
        print(f"Order {self.get_idOrder()} is cancelled")
    
    def __total(self):
        total=sum(self.get_ordered_dishes().values())
        vatTotal=total*self.get_vat()/100
        return total, vatTotal
    
    def display(self):

        print(f"\n--- ORDER N°{self.get_idOrder()} ---")
        print(f"Status: {self.get_order_statut().value}")
     
        for dish, price in self.__ordered_dishes.items():
            print(f"- {dish}: {price}$")
        
        ht, vat=self.__total()
        print(f"Total HT: {ht}$")
        print(f"VAT ({self.get_vat()}%): {vat}$")
        print(f"TOTAL TTC: {ht+vat}$")

cmd1=Command(101)
cmd1.add_dish("Pasta", 12)
cmd1.add_dish("Wine", 8)
cmd1.display()
cmd1.cancel_order()
cmd1.display()

    

    

    


    
