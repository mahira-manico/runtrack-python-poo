class Player:
    #Class representing a football player
    def __init__(self,name,number,position):
        #Initialize personal data and stats at zero
        self.name=name
        self.number=number
        self.position=position
        self.marked_goals=0
        self.decisive_passes=0
        self.yellow_cards_received=0
        self.red_card_received=0
    
    def make_a_goal(self):
        #Increment goal count
        self.marked_goals+=1
        print(f"{self.name} marked a goal!")

    def performADecisivePass(self):
        #Increment assist count
        self.decisive_passes+=1
        print(f"{self.name} performed a decisive pass!")
        
    def receive_A_yellowCard(self):
        #Increment yellow card count
        self.yellow_cards_received+=1
        print(f"{self.name} received a yellow card!")

    def reiceive_A_redCard(self):
        #Increment red card count
        self.red_card_received+=1
        print(f"{self.name} received a red card!")
        
    def displayStatistics(self):
        #Display individual performance stats
        print(f"--{self.name} statistics--")
        print(f"Number: {self.number}")
        print(f"Position: {self.position}")
        print(f"Goals: {self.marked_goals}")
        print(f"Assists: {self.decisive_passes}")
        print(f"Yellow cards: {self.yellow_cards_received}")
        print(f"Red cards: {self.red_card_received}")

class Team:
    #Class managing a group of Player objects
    def __init__(self,name):
        self.name=name
        self.player_list=[] #Internal storage for players
    
    def addPlayer(self,player):
        #Add a Player to the list
        self.player_list.append(player)
        
    def displayPlayersStatistics(self):
        #Iterate through list and call player display method
        for player in self.player_list:
            player.displayStatistics()
        
    def UpdatePlayerStatistics(self,name,goals_to_add,passes_to_add):
        #Search player by name and update their data
        for player in self.player_list:
            if player.name==name:       
                player.marked_goals+=goals_to_add
                player.decisive_passes+=passes_to_add
                print(f"Update successful for {name}")



#test
team1=Team("OM")
team2=Team("PSG")
p1=Player("Mbappé",10,"FW")
p2=Player("Griezmann",11,"MF")
p3=Player("Dembele",7,"FW")
    
team1.addPlayer(p1)
team1.addPlayer(p2)
team2.addPlayer(p3)
    
print(f"Match start: {team1.name} vs {team2.name}")
p1.make_a_goal()
p2.receive_A_yellowCard()

#Display before update
team1.displayPlayersStatistics()
team2.displayPlayersStatistics()

#Player update using team method
team1.UpdatePlayerStatistics("Mbappé",10,3)

#Display after player update
team1.displayPlayersStatistics()
print(f"{team1.name} win!")

