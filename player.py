
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = int(0)
        self.current_gesture = self.select_gesture()
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def select_gesture(self):
        pass
