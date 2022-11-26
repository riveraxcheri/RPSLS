from player import Player
import random

class Ai(Player):
    def __init__(self) -> None:
        super().__init__("Player 2")

    def select_gesture(self):
        self.current_gesture= random.choice(self.gesture_list)
        
