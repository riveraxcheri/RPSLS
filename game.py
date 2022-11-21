import time

class Game:
    def __init__(self) -> None:
        pass

    def welcome_msg(self):
        print ("""Welcome to Rock, Paper, Scissors, Lizard, Spock!
        
        Each match will be the best of 3 games.
        Use the number keys to enter your selection.
        """)

    def game_rules(self):
        self.list = ["Scissors Cut Paper", "Paper Covers Rock", "Rock Crushes Lizard", "Lizard Poisons Spock", "Spock Smashes Scissors", "Scissors Decapitates Lizard", "Lizard Eats Paper", "Paper Disproves Spock", "Spock Vaporizes Rock", "Rock Crushes Scissors"]
        for item in self.list:
            time.sleep(2)
            print (item)
        
