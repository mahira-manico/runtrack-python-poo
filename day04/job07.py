import random

class Cards:
    def __init__(self, color, value):
        self.value=value
        self.color=color

        if value in ["Valet","Dame","Roi"]:
            self.value=10
        elif value=="As":
            self.value=11
        else:
            self.value=int(value)

    def __str__(self):
        return f"{self.color} de {self.value}"
    

class Game:
    def __init__(self):
        self.deck=Deck()
        self.deck.shuffle()
        self.player=Player("You")
        self.dealer=Player("Dealer")
    
    def check_winner(self):
        if self.player.score>21:
            print(f"{self.player.name} lost!")    
        elif self.dealer.score>21 or self.player.score>self.dealer.score:
            print(f"{self.player.name} won!")
        elif self.player.score==self.dealer.score:
            print("Equality!")
        else:
            print(f"{self.dealer.name} won!")

    def start_blackjack(self):
     while True:
     
        my_game=Game()
        my_game.play()
        
        # Une fois la partie finie, on pose la question
        replay=input("\nDo you want to play again ? (yes/no):").lower()
        
        if replay!="yes":
            print("Bye!")
            break

    
    def play(self):
        for turn in range(2):
            self.player.give_card(self.deck.choose_card())
            self.dealer.give_card(self.deck.choose_card())
        
        while True:
            print(f"Your main: {[str(c) for c in self.player.main]} ")
            print(f"Your score: {self.player.calculate_score()}")
            
            if self.player.score>21:
                print("You lost")
                return
            
            choice=input("Do you want to Hit or Stand?: ").lower()

            if choice=="hit":
                self.player.give_card(self.deck.choose_card())
            else:
                break
        
        print(f"Dealer score: {self.dealer.calculate_score()}")
        print(f"Dealer main: {[str(c) for c in self.dealer.main]}")
        while self.dealer.score<17:
            self.dealer.give_card(self.deck.choose_card())
            print(f"New dealer score: {self.dealer.calculate_score()}")
            print(f"Dealer main: {[str(c) for c in self.dealer.main]}")
        
        self.check_winner()
   
            
    
class Deck:
    def __init__(self):
        self.card=[]
        self.create_cards()  
     
    def create_cards(self):
        color=["Coeur","Pique","Trèfle","Carreau"]
        value=[2,3,4,5,6,7,8,9,10,"Valet","Dame","Roi","As"]

        for c in color:
            for v in value:
                new_card=Cards(c, v)
                self.card.append(new_card)
    
    def shuffle(self):
        random.shuffle(self.card)
    
    def choose_card(self):
        return self.card.pop()
    

class Player:
    def __init__(self,name):
        self.score=0
        self.name=name
        self.main=[]
    
    def give_card(self,new_card):
        return self.main.append(new_card)
    
    def calculate_score(self):
        total=0
        as_number=0

        for c in self.main:
            total+=c.value
            if c.value==11:
               as_number+=1
        self.score=total
        while self.score>21 and as_number>0:
                self.score-=10
                as_number-=1
        return self.score
            
my_game=Game()
my_game.start_blackjack()