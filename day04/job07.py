import random

class Cards:
    #Class representing a single playing card
    def __init__(self, color, value):
        self.value=value
        self.color=color

        #Assign numerical values to face cards and aces
        if value in ["Valet","Dame","Roi"]:
            self.value=10
        elif value=="As":
            self.value=11
        else:
            self.value=int(value)

    def __str__(self):
        #Return string representation of the card
        return f"{self.color} de {self.value}"
    

class Game:
    #Main game logic controller
    def __init__(self):
        #Initialize deck and players
        self.deck=Deck()
        self.deck.shuffle()
        self.player=Player("You")
        self.dealer=Player("Dealer")
    
    def check_winner(self):
        #Compare scores to determine the winner
        if self.player.score>21:
            print(f"{self.player.name} lost!")    
        elif self.dealer.score>21 or self.player.score>self.dealer.score:
            print(f"{self.player.name} won!")
        elif self.player.score==self.dealer.score:
            print("Equality!")
        else:
            print(f"{self.dealer.name} won!")

    def start_blackjack(self):
        #Loop to allow multiple game rounds
        while True:
            my_game=Game()
            my_game.play()
            
            #Ask user to replay after the round ends
            replay=input("Do you want to play again ? (yes/no):").lower()
            
            if replay!="yes":
                print("Bye!")
                break

    def play(self):
        #Initial deal of two cards each
        for turn in range(2):
            self.player.give_card(self.deck.choose_card())
            self.dealer.give_card(self.deck.choose_card())
        
        #Player turn loop
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
        
        #Dealer turn logic
        print(f"Dealer score: {self.dealer.calculate_score()}")
        print(f"Dealer main: {[str(c) for c in self.dealer.main]}")
        while self.dealer.score<17:
            self.dealer.give_card(self.deck.choose_card())
            print(f"New dealer score: {self.dealer.calculate_score()}")
            print(f"Dealer main: {[str(c) for c in self.dealer.main]}")
        
        self.check_winner()
    
    
class Deck:
    #Class managing the collection of cards
    def __init__(self):
        self.card=[]
        self.create_cards()  
     
    def create_cards(self):
        #Generate 52 cards for the deck
        color=["Coeur","Pique","Trèfle","Carreau"]
        value=[2,3,4,5,6,7,8,9,10,"Valet","Dame","Roi","As"]

        for c in color:
            for v in value:
                new_card=Cards(c, v)
                self.card.append(new_card)
    
    def shuffle(self):
        #Randomize card order
        random.shuffle(self.card)
    
    def choose_card(self):
        #Draw the top card from the deck
        return self.card.pop()
    

class Player:
    #Class representing a participant in the game
    def __init__(self,name):
        self.score=0
        self.name=name
        self.main=[]
    
    def give_card(self,new_card):
        #Add a card to the player hand
        return self.main.append(new_card)
    
    def calculate_score(self):
        #Calculate total score and handle as adjustment
        total=0
        as_number=0

        for c in self.main:
            total+=c.value
            if c.value==11:
               as_number+=1
        self.score=total
        #Reduce as value from 11 to 1 if score exceeds 21
        while self.score>21 and as_number>0:
                self.score-=10
                as_number-=1
        return self.score
            
#Instantiate and run the game
my_game=Game()
my_game.start_blackjack()