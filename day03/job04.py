class Player:
    def __init__(self,name,number,position,marked_goals,decisive_passes,yellow_cards_received,red_cards_received):
        self.name=name
        self.number=number
        self.position=position
        self.marked_goals=marked_goals
        self.decisive_passes=decisive_passes
        self.yellow_cards_received=yellow_cards_received
        self.red_card_received=red_cards_received

class Team:
    def __init__(self):
        pass