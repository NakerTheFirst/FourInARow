import tkinter as tk
from abc import ABC
from ui import UI


class GUI(UI, ABC):
    def __init__(self, board):
        super().__init__(board)
        self.window = tk.Tk()

    def draw_board(self):
        pass

    def draw_piece(self, column, row, symbol):
        pass

    def get_column_click(self):
        pass

    def show_winner(self, player):
        pass
