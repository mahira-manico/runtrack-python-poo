class Product:
    def __init__(self,name,priceHT,vat): 
        self.name=name #set name
        self.priceHT=priceHT #set price
        self.vat=vat #set vat

    def CalculatePriceVAT(self): #method to return price with vat
        vat=self.priceHT*self.vat/100 #multiply priceHT with vat, divide vat by 100 to convert in percents
        result=self.priceHT+vat #addition of vat + priceHT
        return result

    def display(self): #display method, take result to return it in display
        total=self.CalculatePriceVAT()
        print(f"The {self.name} cost {self.priceHT}$ and the VAT is at {self.vat}%,the price with VAT is: {total}$")

    def changeName(self,name): #method to change name
        self.name=name
        
    def changePrice(self,price): #method to change price
        self.priceHT=price 

    def checkName(self): #display name
        print(f"Product: {self.name}")
     
    def checkPriceHt(self): #display price HT
        print(f"Price without VAT: {self.priceHT}$")
    
    def checkPriceVAT(self): #display price with VAT
        print(f"Price with VAT is: {self.CalculatePriceVAT()}$")

butter=Product("Butter",7,20) #creation of instance

butter.checkName() #display name

display=butter.display() #display all

butter.changeName("chocolate") #change name of product
butter.checkName() #verify changes

butter.changePrice(10) #change price
result=butter.CalculatePriceVAT() #verify price
butter.display() #verify changes

butter.checkPriceHt() #check price HT with new price
butter.checkPriceVAT() #check price with VAT with new price

