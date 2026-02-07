import random

class Character:
    #Character class representing a fighter
    def __init__(self,name,life):
        #Initialize name and health points
        self.name=name
        self.life=life
    
    def attack(self,player):
        #Generate random damage and subtract from opponent life
        damage=random.randint(10,50)
        player.life-=damage
        print(f"--{self.name}-- has attacked --{player.name}-- with |{damage}| Damage!")

    def is_alive(self):
        #Check if the character still has life points
        if self.life>0:
          return True
        return False
    
    def __str__(self):
        #Return string representation of current health
       return f"{self.name}: {self.life} Mana"

class Game:
   #Game class to handle levels and battle loop
   def __init__(self):
      self.level=None
      self.player=None
      self.ennemy=None

   def check_winner(self):
      #Display the winner based on remaining life
      if self.player.life<=0:
          print(f"Game Over! {self.player.name} lost against {self.ennemy.name}!")
      elif self.ennemy.life<=0:
          print(f"{self.player.name} had defeated {self.ennemy.name}!")
   
   def choose_level(self):
      #Menu to select difficulty level
      print("\n                  --Levels--")
      print("--1.Easy -play Frodo: 100 Mana|Orc: |50| Mana--")
      print("--2. Medium -play Aragorn: 90 Mana|Smaug: |120| Mana--")
      print("--3. Hard -play Gandalf: 50 Mana|Balrog: |200| Mana--")
      
      while True:
       try:
        level=int(input("Choose level: "))
        if level in [1,2,3]:
          self.level=level
          break
        else:
          print("Choose a valid number!")
       except ValueError:
          print("Choose a NUMBER!")
   
   def startGame(self):
      #Instantiate player and enemy based on chosen level
      if self.level==1:
          self.player=Character("Frodo",100)
          self.ennemy=Character("Orc",50)
      
      elif self.level==2:
          self.player=Character("Aragorn",90)
          self.ennemy=Character("Smaug",120)
    
      elif self.level==3:
          self.player=Character("Gandalf",50)
          self.ennemy=Character("Balrog",200)
    
      print(f"\nGame start! {self.player} VS {self.ennemy}!|Level: {self.level}")
      print("-----------------------------------------------------")    

      while True:
        try:
         if self.player.is_alive() and self.ennemy.is_alive():

            print(f"\n|----{self.player}----|")
            print(f"|----{self.ennemy}----|\n")

            enter=int(input("Press 1 to attack!\n"))
            if enter==1:
               self.player.attack(self.ennemy)
               if self.ennemy.is_alive():
                  self.ennemy.attack(self.player)
            else:
               print("PRESS 1 ONLY!")
            self.check_winner()
            if not self.player.is_alive() or not self.ennemy.is_alive():
                break
            
        except ValueError:
            print("ONLY 1!")

if __name__=="__main__":
 #Main execution block
 my_game=Game()
 my_game.choose_level()
 my_game.startGame()


