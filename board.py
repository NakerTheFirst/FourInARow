class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(9)] for _ in range(6)]
        self.gui_handler = None  # Set in Engine initialiser

    def display(self):
        pass

    def display_console(self):
        """Developer tool: display the board in console"""
        pass

    def place_piece(self, column, symbol):
        pass

    def is_full(self):
        pass

    def check_win(self):
        pass

