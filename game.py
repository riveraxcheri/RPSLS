# import time
from human import Human
from ai import Ai

class Game:
    def __init__(self) -> None:
        self.player_one= Human()
        self.player_two= Ai()


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
            # time.sleep(2)
            print (item)

    def choose_players(self):
        user_input=input("How many players? (please enter 1 or 2) ")
        if user_input == "1":
            self.new_round()
        elif user_input == "2":
            self.player_two= Human()
            self.new_round()
        else: 
            print("Please input either 1 or 2: ")

    def determine_winner(self):
        if self.player_one.current_gesture == self.player_two.current_gesture:
                print("It's a Tie!")
                self.new_round()
        elif self.player_one.current_gesture == "Rock" and (self.player_two.current_gesture == "Paper" or self.player_two.current_gesture == "Spock"):
                self.player_two.score= self.player_two.score + int(1)
                print(f"Player 2 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()
        elif self.player_one.current_gesture == "Rock" and (self.player_two.current_gesture == "Scissors" or self.player_two.current_gesture == "Lizard"):
                self.player_one.score= self.player_one.score + int(1)
                print(f"Player 1 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()
        elif self.player_one.current_gesture == "Paper" and (self.player_two.current_gesture == "Scissors" or self.player_two.current_gesture == "Lizard"):
                self.player_two.score= self.player_two.score + int(1)
                print(f"Player 2 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()
        elif self.player_one.current_gesture == "Paper" and (self.player_two.current_gesture == "Rock" or self.player_two.current_gesture == "Spock"):
                self.player_one.score= self.player_one.score + int(1)
                print(f"Player 1 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()
        elif self.player_one.current_gesture == "Scissors" and (self.player_two.current_gesture == "Rock" or self.player_two.current_gesture == "Spock"):
                self.player_two.score= self.player_two.score + int(1)
                print(f"Player 2 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()
        elif self.player_one.current_gesture == "Scissors" and (self.player_two.current_gesture == "Paper" or self.player_two.current_gesture == "Lizard"):
                self.player_one.score= self.player_one.score + int(1)
                print(f"Player 1 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()
        elif self.player_one.current_gesture == "Lizard" and (self.player_two.current_gesture == "Rock" or self.player_two.current_gesture == "Scissors"):
                self.player_two.score= self.player_two.score + int(1)
                print(f"Player 2 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()
        elif self.player_one.current_gesture == "Lizard" and (self.player_two.current_gesture == "Paper" or self.player_two.current_gesture == "Spock"):
                self.player_one.score= self.player_one.score + int(1)
                print(f"Player 1 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()
        elif self.player_one.current_gesture == "Spock" and (self.player_two.current_gesture == "Paper" or self.player_two.current_gesture == "Lizard"):
                self.player_two.score= self.player_two.score + int(1)
                print(f"Player 2 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()
        elif self.player_one.current_gesture == "Spock" and (self.player_two.current_gesture == "Rock" or self.player_two.current_gesture == "Scissors"):
                self.player_one.score= self.player_one.score + int(1)
                print(f"Player 1 Wins! Score: P1:{self.player_one.score} P2:{self.player_two.score}")
                self.new_round()

    def new_round(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.player_one.select_gesture()
            self.player_two.select_gesture()
            print (f"Player 1 selected {self.player_one.current_gesture}")
            print (f"Player 2 selected {self.player_two.current_gesture}")
            self.determine_winner()
            return
        else:
            if self.player_one.score >= 3:
                print(f"{self.player_one.name} Wins! \n Game Over")
                return
            elif self.player_two.score >= 3:
                print(f"{self.player_two.name} Wins! \n Game Over")
                return

    def run_game(self):
        self.welcome_msg()
        self.game_rules()
        self.choose_players()