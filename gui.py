from numpy import random
import tkinter as tk
from abc import ABC
from ai_player import AIPlayer
from ui import UI


class GUI(UI, ABC):
    def __init__(self, board):
        super().__init__(board)
        self.__root = tk.Tk()
        self.__bottom_frame = tk.Frame(self.__root, width=640, height=115, bg="#4C4246")
        self.__orb_columns = []
        self.__orbs = []
        self.__text = tk.StringVar()
        self.__text.set(f"{self.board.players[self.board.current_player].name}, click a column to place your piece")
        self.__textbox_frame = None
        self.__text_info = None
        self.waiting_for_ai = False

    def display(self):
        self.__setup_root()

        # Setup bottom frame
        self.__bottom_frame.pack(side="bottom", fill="x")
        self.__draw_textbox()

        # Draw orb columns
        orb_frame = self.__draw_orb_frame()
        self.__draw_orbs_columns(orb_frame)
        self.__root.mainloop()

    def __setup_root(self):
        self.__root.title("Four In A Row")
        self.__root.geometry("640x600")
        self.__root.configure(bg="#2E282A")
        icon = tk.PhotoImage(file="icon.ico")
        self.__root.iconphoto(False, icon)

    def __draw_textbox(self):
        self.__textbox_frame = tk.Frame(self.__bottom_frame, width=310, height=43, bg="#237373")
        self.__textbox_frame.pack(pady=36)
        self.__textbox_frame.grid_propagate(False)

        self.__text_info = tk.Label(self.__textbox_frame, textvariable=self.__text,
                                    font=("Ubuntu", -12), bg="#237373", fg="#FFF")
        self.__text_info.grid(sticky="nsew", padx=10, pady=10)
        self.__textbox_frame.columnconfigure(0, weight=1)
        self.__textbox_frame.rowconfigure(0, weight=1)

    def __draw_orb_frame(self):
        orb_frame = tk.Frame(self.__root, width=530, height=375, bg="#2E282A")
        orb_frame.pack(padx=55, pady=55, fill="both")
        return orb_frame

    def __draw_orbs_columns(self, orb_frame):
        for i in range(9):
            column = tk.Canvas(orb_frame, width=50, height=375, bg="#2E282A", bd=0, highlightthickness=0)
            column.place(x=0 + 50*i + 10*i)
            column.bind('<Button-1>', self.__make_move(i))
            self.__orb_columns.append(column)
            self.__orbs.append(self.__create_orb_column(column))

    @staticmethod
    def __create_orb_column(column):
        orb_column = []
        for j in range(6):
            orb = column.create_oval(0, j * 50 + j * 15, 48, 48 + j * 50 + j * 15, fill="#A09297", outline="")
            orb_column.append(orb)
        return orb_column

    def __make_move(self, column):
        def __handle_click(event=None):
            if self.board.is_game_over or isinstance(self.board.players[self.board.current_player], AIPlayer):
                return

            if self.board.is_column_full(column):
                self.__text.set(f"Column {column} is full. Please choose another column.")
                return

            for row in reversed(range(6)):
                if self.board.grid[row][column] != "o":
                    continue

                self.__execute_move(column, row)
                break

            if not self.board.is_game_over and isinstance(self.board.players[self.board.current_player], AIPlayer):
                self.__root.after(random.randint(1000, 2500), self.__make_ai_move)

        return __handle_click

    def __make_ai_move(self):
        if isinstance(self.board.players[1], AIPlayer):
            while True:
                column = self.board.players[1].choose_column(self.board)
                if not self.board.is_column_full(column):
                    break
            for row in reversed(range(6)):
                if self.board.grid[row][column] == "o":
                    self.__execute_move(column, row)
                    break

    def __execute_move(self, column, row):
        self.board.grid[row][column] = self.board.players[self.board.current_player].symbol
        self.__change_orb_colour(column, row, self.__get_orb_colour())

        if self.board.check_win():
            self.__text.set(f"{self.board.players[self.board.current_player].name} wins! Congratulations!")
            self.board._is_game_over = True
        else:
            self.board.switch_player()
            self.__update_textbox_text()

        self.__change_textbox_colour()

    def __change_orb_colour(self, column, row, colour):
        self.__orb_columns[column].itemconfig(self.__orbs[column][row], fill=colour)

    def __change_textbox_colour(self):
        colour = self.__get_orb_colour()
        if self.__textbox_frame and self.__text_info:
            self.__textbox_frame.configure(bg=colour)
            self.__text_info.configure(bg=colour)

    def __get_orb_colour(self):
        return "#CD5334" if self.board.current_player else "#237373"

    def __update_textbox_text(self):
        player_name = self.board.players[self.board.current_player].name
        if player_name != 'AI':
            self.__text.set(f"{player_name}, click a column to place your piece")
        else:
            self.__text.set(f"{player_name} is taking its turn")
