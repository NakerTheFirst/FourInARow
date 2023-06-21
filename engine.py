from console_interface import ConsoleInterface
from gui import GUI
from board import Board


class Engine:
    def __init__(self):
        self.__board = Board()
        self.__ui = self.__choose_interface()

    def play(self):
        # Initialise Console Interface
        if isinstance(self.__ui, ConsoleInterface):
            while not self.__board.is_game_over:
                player = self.__board.players[self.__board.current_player]
                self.__ui.display()

                while True:
                    column = player.choose_column(self.__board)
                    if not self.__board.is_column_full(column):
                        break
                    print(f"Column {column} is full. Please choose another column.")
                self.__board.place_piece(column, player.symbol)

                # Win/draw checks
                if self.__board.check_win():
                    self.__ui.display()
                    print(f"{player.name} wins!")
                elif self.__board.is_board_full():
                    self.__board.is_game_over = True
                    self.__ui.display()
                    print("It's a draw!")

                if self.__board.is_game_over:
                    break

                else:
                    self.__board.switch_player()

        # Initialise GUI
        elif isinstance(self.__ui, GUI):
            self.__ui.display()

    def __choose_interface(self):
        while True:
            choice = input("Choose an interface ('console' or 'gui'): ")
            if choice.lower() == 'console':
                return ConsoleInterface(self.__board)
            elif choice.lower() == 'gui':
                return GUI(self.__board)
            else:
                print("Invalid input. Please enter 'console' or 'gui'.")
