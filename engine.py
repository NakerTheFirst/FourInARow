from ai_player import AIPlayer
from board import Board
from gui_handler import GuiHandler
from human_player import HumanPlayer


class Engine:
    def __init__(self):
        self.players = [HumanPlayer('Player 1', '1'), AIPlayer('Player 2', '2')]
        self.board = Board()
        self.gui_handler = GuiHandler(self.board)
        self.board.gui_handler = self.gui_handler  # Set GuiHandler reference in Board
        self.current_player = 0
        self.ui = None

    def play(self):
        is_over = False
        while not is_over:
            player = self.players[self.current_player]
            self.board.display_console()

            while True:  # Loop until a valid column is selected
                column = player.choose_column(self.board)
                if not self.board.is_column_full(column):
                    break
                print(f"Column {column} is full. Please choose another column.")
            self.board.place_piece(column, player.symbol)

            # Win/draw checks
            if self.board.check_win():
                is_over = True
                print(f"{player.name} wins!")
            elif self.board.is_full():
                is_over = True
                print("It's a draw!")
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def choose_interface(self):
        while True:
            choice = input("Choose an interface ('console' or 'gui'): ")
            if choice.lower() in ['console', 'gui']:
                self.ui = choice.lower()
                break
            else:
                print("Invalid input. Please enter 'console' or 'gui'.")
