class Board:
    def __init__(self):
        self.grid = [['o' for _ in range(9)] for _ in range(6)]
        self.gui_handler = None  # Set in Engine initialiser

    def display(self):
        pass

    def display_console(self):
        """Developer tool: display the board in console"""
        print()
        for row in range(6):
            for col in range(9):
                print(self.grid[row][col], end=" ")
            print()
        print()

    def place_piece(self, column, symbol):
        for row in reversed(self.grid):
            if row[column] == 'o':
                row[column] = symbol
                break
        self.check_win()

    def is_column_full(self, column):
        for row in self.grid:
            if row[column] == 'o':
                return False
        return True

    def is_full(self):
        for col in range(9):
            if not self.is_column_full(col):  # If any column is not full
                return False  # The board is not full
        return True

    def check_win(self):
        # Check rows
        for row in self.grid:
            for i in range(len(row) - 3):
                if row[i] == row[i+1] == row[i+2] == row[i+3] != 'o':
                    return True

        # Check columns
        for j in range(len(self.grid[0])):
            for i in range(len(self.grid) - 3):
                if self.grid[i][j] == self.grid[i+1][j] == self.grid[i+2][j] == self.grid[i+3][j] != 'o':
                    return True

        # Check top-left to bottom-right
        for i in range(len(self.grid) - 3):
            for j in range(len(self.grid[0]) - 3):
                if self.grid[i][j] == self.grid[i+1][j+1] == self.grid[i+2][j+2] == self.grid[i+3][j+3] != 'o':
                    return True

        # Check top-right to bottom-left
        for i in range(len(self.grid) - 3):
            for j in range(3, len(self.grid[0])):
                if self.grid[i][j] == self.grid[i+1][j-1] == self.grid[i+2][j-2] == self.grid[i+3][j-3] != 'o':
                    return True

        return False
