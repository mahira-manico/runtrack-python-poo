#creation of class "animal"
class Animal:
    def __init__(self,age=0,name=""): #initialization in settings of age and name
        self.age=age
        self.name=name

    def __str__(self): #return age
        return f"This animal is {self.age} years old."
  
    def aging(self): #add +1 to age everytime the function is called
        self.age+=1     
        print(f"this animal is now {self.age} years old!") #display new age

    def naming(self, name): #name the animal 
        return f"This animal is named {name}"

cat=Animal()
print(cat) #display age of the animal

display_name=cat.naming("Vanilla") 
print(display_name) #display name of the animal

display_aging=cat.aging() #age cat +1
dipslay_aging=cat.aging() #age cat +1 wich give +2

dog=Animal() #creation of object dog
print(dog)

display_name=dog.naming("Ponpon") #name the dog
print(display_name)

display_aging=dog.aging() #age the dog





