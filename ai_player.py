from player import Player
import random


class AIPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def choose_column(self, board):
        while True:
            column = random.randint(0, 8)
            if not board.is_column_full(column):
                return column
