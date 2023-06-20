from console_interface import ConsoleInterface
from gui import GUI
from board import Board


class Engine:
    def __init__(self):
        self.board = Board()
        self.ui = self.choose_interface()

    def play(self):
        # Console interface
        if isinstance(self.ui, ConsoleInterface):
            is_over = False
            while not is_over:
                player = self.board.players[self.board.current_player]
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
                    self.board.switch_player()

        # Graphical User Interface
        elif isinstance(self.ui, GUI):
            self.ui.display()

    def choose_interface(self):
        while True:
            # choice = input("Choose an interface ('console' or 'gui'): ")
            choice = 'gui'
            if choice.lower() == 'console':
                return ConsoleInterface(self.board)
            elif choice.lower() == 'gui':
                return GUI(self.board)
            else:
                print("Invalid input. Please enter 'console' or 'gui'.")
