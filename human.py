from player import Player

class Human(Player):

    def __init__(self) -> None:
        super().__init__()
        self.name = input("What is your name? ")

    def select_gesture(self):
        user_input= (input("""
        Which gesture would you like to use?
        Choose 0 for Rock
        Choose 1 for Paper
        Choose 2 for Scissors
        Choose 3 for Lizard
        Choose 4 for Spock
        
        Enter choice number here: """))
        if user_input == 0:
            self.current_gesture = self.gesture_list[0]
        elif user_input == 1:
            self.current_gesture = self.gesture_list[1]
        elif user_input == 2:
            self.current_gesture = self.gesture_list[2]
        elif user_input == 3:
            self.current_gesture = self.gesture_list[3]
        elif user_input == 4:
            self.current_gesture = self.gesture_list[4]
        else:
            print ("Oops! Please enter one of the 5 number options.")

