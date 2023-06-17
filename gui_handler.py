import tkinter as tk


class GuiHandler:
    def __init__(self, board):
        self.board = board
        self.window = tk.Tk()

    def draw_board(self):
        pass

    def draw_piece(self, column, row, symbol):
        pass

    def get_column_click(self):
        pass

    def show_winner(self, player):
        pass
