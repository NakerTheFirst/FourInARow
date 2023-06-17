from player import Player


class HumanPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def choose_column(self, board):
        while True:
            column = input(f"{self.name}, choose a column to place your piece (0-8): ")
            if column.isdigit() and 0 <= int(column) <= 8:  # Check if the input is a valid column number
                return int(column)
            else:
                print("Invalid input. Please enter a number between 0 and 8.")
