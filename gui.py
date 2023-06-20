from numpy import random
import tkinter as tk
from abc import ABC
from ai_player import AIPlayer
from ui import UI

# TODO: Modularise the methods, reduce the spaghetti level
# TODO: Add class diagram
# TODO: Add docs
# TODO: Update methods' and attributes' access specifiers


class GUI(UI, ABC):
    def __init__(self, board):
        super().__init__(board)
        self.root = tk.Tk()
        self.bottom_frame = tk.Frame(self.root, width=640, height=115, bg="#4C4246")
        self.orb_columns = []
        self.orbs = []
        self.text = tk.StringVar()
        self.text.set(f"{self.board.players[self.board.current_player].name}, click a column to place your piece")
        self.textbox_frame = None
        self.text_info = None
        self.waiting_for_ai = False

    def display(self):
        """The draw everything method"""
        self.root.title("Four In A Row")
        self.root.geometry("640x600")
        self.root.configure(bg="#2E282A")
        icon = tk.PhotoImage(file="icon.ico")
        self.root.iconphoto(False, icon)
        self.bottom_frame.pack(side="bottom", fill="x")

        # Draw separate interface elements
        self.draw_textbox(self.text)
        self.draw_orbs_columns(self.draw_orb_frame())

        self.root.mainloop()

    def draw_textbox(self, text):
        self.textbox_frame = tk.Frame(self.bottom_frame, width=310, height=43, bg="#237373")
        self.textbox_frame.pack(pady=36)
        self.textbox_frame.grid_propagate(False)

        self.text_info = tk.Label(self.textbox_frame, textvariable=self.text, font=("Ubuntu", -12), bg="#237373", fg="#FFF")
        self.text_info.grid(sticky="nsew", padx=10, pady=10)
        self.textbox_frame.columnconfigure(0, weight=1)
        self.textbox_frame.rowconfigure(0, weight=1)

    def draw_orb_frame(self):
        orb_frame = tk.Frame(self.root, width=530, height=375, bg="#2E282A")
        orb_frame.pack(padx=55, pady=55, fill="both")
        return orb_frame

    def draw_orbs_columns(self, orb_frame):
        for i in range(9):
            column = tk.Canvas(orb_frame, width=50, height=375, bg="#2E282A", bd=0, highlightthickness=0)
            column.place(x=0 + 50*i + 10*i)
            column.bind('<Button-1>', self.handle_click(i))
            self.orb_columns.append(column)

            orb_column = []
            for j in range(6):
                orb = column.create_oval(0, j * 50 + j * 15, 48, 48 + j * 50 + j * 15, fill="#A09297", outline="")
                orb_column.append(orb)
            self.orbs.append(orb_column)

        return self.orb_columns, self.orbs

    def handle_click(self, column):
        def _handle_click(event):
            if not self.board.is_game_over and not isinstance(self.board.players[self.board.current_player], AIPlayer):
                if self.board.is_column_full(column):
                    self.text.set(f"Column {column} is full. Please choose another column.")
                else:
                    for row in reversed(range(6)):
                        if self.board.grid[row][column] == "o":
                            self.board.grid[row][column] = self.board.players[self.board.current_player].symbol
                            self.change_orb_colour(column, row, self.get_orb_colour())

                            if self.board.check_win():
                                self.text.set(f"{self.board.players[self.board.current_player].name} wins!")
                                self.board.is_game_over = True
                            else:
                                self.board.switch_player()
                                self.update_textbox_text()

                            self.change_textbox_colour()
                            break
            if not self.board.is_game_over and isinstance(self.board.players[self.board.current_player], AIPlayer):
                self.root.after(random.randint(1000, 2500), self.make_ai_move)

        return _handle_click

    def change_orb_colour(self, column, row, colour):
        self.orb_columns[column].itemconfig(self.orbs[column][row], fill=colour)

    def change_textbox_colour(self):
        colour = self.get_orb_colour()
        if self.textbox_frame and self.text_info:
            self.textbox_frame.configure(bg=colour)
            self.text_info.configure(bg=colour)

    def get_orb_colour(self):
        return "#CD5334" if self.board.current_player else "#237373"

    def update_textbox_text(self):
        player_name = self.board.players[self.board.current_player].name
        if player_name != 'AI':
            self.text.set(f"{player_name}, click a column to place your piece")
        else:
            self.text.set(f"{player_name} is taking its turn")

    def make_ai_move(self):
        if isinstance(self.board.players[1], AIPlayer):
            while True:
                column = self.board.players[1].choose_column(self.board)
                if not self.board.is_column_full(column):
                    break
            for row in reversed(range(6)):
                if self.board.grid[row][column] == "o":
                    self.board.grid[row][column] = self.board.players[1].symbol
                    self.change_orb_colour(column, row, self.get_orb_colour())
                    if self.board.check_win():
                        self.text.set(f"{self.board.players[1].name} wins!")
                        self.board.is_game_over = True
                    else:
                        self.board.switch_player()
                        self.update_textbox_text()
                    self.change_textbox_colour()
                    break
