from player import Player

class Human(Player):

    def __init__(self) -> None:
        user_name = input("What is your name? ")
        super().__init__(self)
        self.name = user_name

    def select_gesture(self):
        user_input= (input(f"""
        Hello, {self.name}
        Which gesture would you like to use?
        Choose 0 for Rock
        Choose 1 for Paper
        Choose 2 for Scissors
        Choose 3 for Lizard
        Choose 4 for Spock
        
        Enter choice number here: """))
        if user_input == "0":
            self.current_gesture = "Rock"
        elif user_input == "1":
            self.current_gesture = "Paper"
        elif user_input == "2":
            self.current_gesture = "Scissors"
        elif user_input == "3":
            self.current_gesture = "Lizard"
        elif user_input == "4":
            self.current_gesture = "Spock"
        else:
            print ("Oops! Please enter one of the 5 number options.")