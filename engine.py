from ai_player import AIPlayer
from board import Board
from console_interface import ConsoleInterface
from gui import GUI
from human_player import HumanPlayer


class Engine:
    def __init__(self):
        self.players = [HumanPlayer('Player 1', '1'), AIPlayer('Player 2', '2')]
        self.board = Board()
        self.current_player = 0
        self.ui = None

    def play(self):
        self.choose_interface()
        self.choose_players()
        is_over = False
        while not is_over:
            player = self.players[self.current_player]
            self.ui.display()

            while True:
                column = player.choose_column(self.board)
                if not self.board.is_column_full(column):
                    break
                print(f"Column {column} is full. Please choose another column.")
            self.board.place_piece(column, player.symbol)

            # Win/draw checks
            if self.board.check_win():
                is_over = True
                self.ui.display()
                print(f"{player.name} wins!")
            elif self.board.is_full():
                is_over = True
                self.ui.display()
                print("It's a draw!")
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def choose_interface(self):
        while True:
            choice = input("Choose an interface ('console' or 'gui'): ")
            if choice.lower() == 'console':
                self.ui = ConsoleInterface(self.board)
                break
            elif choice.lower() == 'gui':
                self.ui = GUI(self.board)
            else:
                print("Invalid input. Please enter 'console' or 'gui'.")

    def choose_players(self):
        while True:
            choice = input("Choose your opponent ('human' or 'ai'): ")
            if choice.lower() == 'human':
                self.players = [HumanPlayer('Player 1', '1'), HumanPlayer('Player 2', '2')]
                break
            elif choice.lower() == 'ai':
                self.players = [HumanPlayer('Player 1', '1'), AIPlayer('Player 2', '2')]
                break
            else:
                print("Invalid input. Please enter 'human' or 'ai'.")
