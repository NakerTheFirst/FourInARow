from ui import UI
from abc import ABC


class ConsoleInterface(UI, ABC):
    def __init__(self, board):
        super().__init__(board)

    def display(self):
        print()
        for row in range(6):
            for col in range(9):
                print(self.board.grid[row][col], end=" ")
            print()
        print()
