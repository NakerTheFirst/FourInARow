from human_player import HumanPlayer
from ai_player import AIPlayer


class Board:
    def __init__(self):
        self.__grid = [['o' for _ in range(9)] for _ in range(6)]
        self.__players = self.__choose_players()
        self.__current_player = 0
        self.__is_game_over = False

    @staticmethod
    def __choose_players():
        while True:
            choice = input("Choose your opponent 'human' or 'ai': ")
            if choice.lower() == 'human':
                return HumanPlayer('Player 1', '1'), HumanPlayer('Player 2', '2')
            elif choice.lower() == 'ai':
                return HumanPlayer('Player 1', '1'), AIPlayer('AI', '2')
            else:
                print("Invalid input. Please enter 'human' or 'ai'.")

    def switch_player(self):
        self.__current_player = 1 - self.__current_player

    def place_piece(self, column, symbol):
        for row in reversed(self.__grid):
            if row[column] == 'o':
                row[column] = symbol
                break
        self.check_win()

    def is_column_full(self, column):
        return 'o' not in (row[column] for row in self.__grid)

    def is_board_full(self):
        return all(self.is_column_full(col) for col in range(9))

    def _is_consecutive(self, coords):
        vals = [self.__grid[i][j] for i, j in coords]
        return all(val == vals[0] != 'o' for val in vals)

    def check_win(self):
        rows = [[(i, j+n) for n in range(4)] for i in range(6) for j in range(6)]
        cols = [[(i+n, j) for n in range(4)] for i in range(3) for j in range(9)]
        diags1 = [[(i+n, j+n) for n in range(4)] for i in range(3) for j in range(6)]
        diags2 = [[(i+n, j-n) for n in range(4)] for i in range(3) for j in range(3, 9)]

        for group in rows, cols, diags1, diags2:
            if any(self._is_consecutive(coords) for coords in group):
                self.__is_game_over = True
                return True
        return False

    @property
    def grid(self):
        return self.__grid

    @property
    def players(self):
        return self.__players

    @property
    def current_player(self):
        return self.__current_player

    @property
    def is_game_over(self):
        return self.__is_game_over

    @is_game_over.setter
    def is_game_over(self, value):
        if isinstance(value, bool):
            self.__is_game_over = value
        else:
            raise ValueError("is_game_over must be a boolean")
