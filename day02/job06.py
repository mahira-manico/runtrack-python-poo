from enum import Enum

# Define fixed statuses for the order
class Status(Enum):
    IN_PROGRESS = "In progress"
    FINISHED = "Finished"
    CANCELED = "Canceled"

class Command:
    def __init__(self, idOrder):
        # Initialize private attributes
        self.__idOrder = idOrder
        self.__ordered_dishes = {} # Dictionary to store dish names and prices
        self.__order_statut = Status.IN_PROGRESS
        self.__vat = 20 # VAT rate at 20%
    
    # Getters and Setters
    def get_idOrder(self):
        return self.__idOrder    
    
    def set_idOrder(self, new_order):
        self.__idOrder = new_order
    
    def get_ordered_dishes(self):
        return self.__ordered_dishes
    
    def set_ordered_dishes(self, new_ordered_dishes):
        self.__ordered_dishes = new_ordered_dishes
    
    def get_order_statut(self):
        return self.__order_statut
    
    def get_vat(self):
        return self.__vat
    
    # Method to add a new dish to the dictionary
    def add_dish(self, new_dish, price):
        # Only add if the order is still in progress
        if self.get_order_statut() == Status.IN_PROGRESS:
            self.get_ordered_dishes()[new_dish] = price
            print(f"{new_dish} at {price}$ added to order")
        else:
            print("Error: Cannot add dish to a finished or canceled order.")
    
    # Method to cancel the order and clear the dishes
    def cancel_order(self):
        self.__order_statut = Status.CANCELED # Set status to Canceled
        self.get_ordered_dishes().clear() # Empty the dictionary
        print(f"Order {self.get_idOrder()} is cancelled")
    
    # Method to finish the order
    def finish_order(self):
        self.__order_statut = Status.FINISHED # Set status to Finished
        print(f"Order {self.get_idOrder()} is now finished")

    # Private method to calculate total price and VAT
    def __total(self):
        # sum() the values (prices) from the dictionary
        total = sum(self.get_ordered_dishes().values())
        vatTotal = total * self.get_vat() / 100
        return total, vatTotal
    
    # Method to display order details
    def display(self):
        print(f"\n--- ORDER N°{self.get_idOrder()} ---")
        # .value gets the string "In progress" from the Enum
        print(f"Status: {self.get_order_statut().value}")
     
        # Loop through the dictionary to show each dish
        for dish, price in self.get_ordered_dishes().items():
            print(f"- {dish}: {price}$")
        
        # Get HT and VAT from the private __total method
        ht, vat = self.__total()
        print(f"Total HT: {ht:.2f}$")
        print(f"VAT ({self.get_vat()}%): {vat:.2f}$")
        print(f"TOTAL TTC: {ht + vat:.2f}$")

# Test the code
cmd1 = Command(101)
cmd1.add_dish("Pasta", 12)
cmd1.add_dish("Wine", 8)
cmd1.display()

# Test cancellation
cmd1.cancel_order()
cmd1.display()


    
