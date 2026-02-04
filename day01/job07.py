class Character:
    def __init__(self):
        self.x=0 #initialization of variables
        self.y=0

    def left(self): #move to the left
        self.x-=1

    def right(self): #move to the right
        self.x=1

    def up(self): #move up
        self.y-=1

    def down(self): #move down
        self.y+=1
    
    def position(self): #return x and y in tuple
       return self.x,self.y
    
fairy=Character() #creation of instance
fairy.down() #move methods
fairy.right()

pos=fairy.position() #take the tuple
print(pos) #dipslay the tuple



