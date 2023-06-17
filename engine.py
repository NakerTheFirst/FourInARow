from abc import abstractmethod, ABCMeta
import tkinter as tk
from ai_player import AIPlayer
from board import Board
from gui_handler import GuiHandler
from human_player import HumanPlayer


class Engine:
    def __init__(self):
        self.players = [HumanPlayer('Player 1', 'red'), AIPlayer('Player 2', 'gold')]
        self.board = Board()
        self.gui_handler = GuiHandler(self.board)
        self.board.gui_handler = self.gui_handler  # Set GuiHandler reference in Board
        self.current_player = 0

    def play(self):
        pass

    def switch_player(self):
        self.current_player = 1 - self.current_player
