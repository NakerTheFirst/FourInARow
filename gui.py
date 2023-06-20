import tkinter as tk
from abc import ABC
from ui import UI

# TODO: Update text based on current player
# TODO: Add game logic to GUI
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
        self.text = "Player 1, click a column to place your piece"
        self.textbox_frame = None
        self.text_info = None

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

        string_var = tk.StringVar()
        string_var.set(text)

        self.text_info = tk.Label(self.textbox_frame, textvariable=string_var, font=("Ubuntu", -12), bg="#237373", fg="#FFF")
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
            for row in reversed(range(6)):
                if self.board.grid[row][column] == "o":
                    self.board.grid[row][column] = self.board.players[self.board.current_player].symbol
                    self.change_orb_colour(column, row, self.get_orb_colour())
                    self.change_textbox_colour()
                    self.board.switch_player()
                    # self.board.check_win()
                    break
        return _handle_click

    def change_orb_colour(self, column, row, colour):
        self.orb_columns[column].itemconfig(self.orbs[column][row], fill=colour)

    def change_textbox_colour(self):
        colour = self.get_textbox_colour()
        if self.textbox_frame and self.text_info:
            self.textbox_frame.configure(bg=colour)
            self.text_info.configure(bg=colour)

    def get_orb_colour(self):
        return "#CD5334" if self.board.current_player else "#237373"

    def get_textbox_colour(self):
        return "#237373" if self.board.current_player else "#CD5334"
