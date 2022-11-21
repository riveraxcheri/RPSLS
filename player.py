
class Player:
    def __init__(self, name, score, gesture) -> None:
        self.name = name
        self.score = int(score)
        self.current_gesture = gesture
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def select_gesture(self):
        pass
