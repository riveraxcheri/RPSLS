import time
from player import Player
from human import Human
from ai import Ai

class Game:
    def __init__(self) -> None:
        self.player_one= Player(Human)
        self.player_two= Player(Ai)


    def welcome_msg(self):
        print ("""
        Welcome to Rock, Paper, Scissors, Lizard, Spock!
        
        Each match will be the best of 3 games.
        Use the number keys to enter your selection.
        Here are the Game Rules:
        """)

    def game_rules(self):
        self.list = ["Scissors Cut Paper", "Paper Covers Rock", "Rock Crushes Lizard", "Lizard Poisons Spock", "Spock Smashes Scissors", "Scissors Decapitates Lizard", "Lizard Eats Paper", "Paper Disproves Spock", "Spock Vaporizes Rock", "Rock Crushes Scissors"]
        for item in self.list:
            time.sleep(2)
            print (item)

    def choose_players(self):
        user_input=input("How many players? (please enter 1 or 2) ")
        if user_input == 1:
            self.one_player()
        elif user_input == 2:
            self.two_player()
        else: 
            print("Please input either 1 or 2: ")

    def one_player(self):
        print (f"Player 1 selected {self.player_one.select_gesture()}")
        print (f"Player 2 selected {self.player_two.select_gesture()}")
        self.determine_winner()


    def two_player(self):
        self.player_two= Player(Human)
        print (f"Player 1 selected {self.player_one.select_gesture()}")
        print (f"Player 2 selected {self.player_two.select_gesture()}")
        self.determine_winner()

# 0:Rock/ 1:Paper/ 2:Scissors/ 3:Lizard/ 4:Spock

    def determine_winner(self):
        p1_score = self.player_one.score
        p2_score = self.player_two.score
        p1_gesture = self.player_one.current_gesture
        p2_gesture = self.player_two.current_gesture
        while p1_score < 2:
            if p1_gesture == 0:
                if p2_gesture == 0:
                    print("It's a Tie!")
                elif p2_gesture == 1:
                    p2_score = p2_score + int(1)
                    print(f"Player 2 Wins! Score: P1:{p1_score} P2:{p2_score}")
                elif p2_gesture == 2:
                    p1_score = p1_score + int(1)
                    print(f"Player 1 Wins! Score: P1:{p1_score} P2:{p2_score}")
                elif p2_gesture == 3:
                    p1_score = p1_score + int(1)
                    print(f"Player 1 Wins! Score: P1:{p1_score} P2:{p2_score}")
                elif p2_gesture == 4:
                    p2_score = p2_score + int(1)
                    print(f"Player 2 Wins! Score: P1:{p1_score} P2:{p2_score}")
        
