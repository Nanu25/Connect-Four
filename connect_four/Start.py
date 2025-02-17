import tkinter as tk
from tkinter import ttk
from connect_four.GUI.gui import Ui
from connect_four.domain.board import Board
from connect_four.domain.computer import Computer
from connect_four.domain.player import Player

EASY = 1
MEDIUM = 2
HARD = 3
EXTREME_HARD = 4


class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")

        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=[12, 8], font=('Arial', 10))
        style.configure('TFrame', background='#f0f0f0')

        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(pady=10, expand=True, fill=tk.BOTH)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Game Mode")
        self.notebook.add(self.tab2, text="Player Setup")

        self.setup_game_mode_tab()
        self.setup_player_setup_tab()

    def setup_game_mode_tab(self):
        frame = ttk.Frame(self.tab1, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(frame, text="Select Game Mode",
                          font=("Arial", 16, "bold"))
        title.pack(pady=(0, 20))

        self.option_var = tk.IntVar(value=1)

        modes_frame = ttk.Frame(frame)
        modes_frame.pack(fill=tk.X, pady=10)

        ttk.Radiobutton(modes_frame,
                        text="Human vs Computer",
                        variable=self.option_var,
                        value=1,
                        command=self.toggle_difficulty,
                        style='TRadiobutton').pack(pady=5)

        ttk.Radiobutton(modes_frame,
                        text="Human vs Human",
                        variable=self.option_var,
                        value=2,
                        command=self.toggle_difficulty,
                        style='TRadiobutton').pack(pady=5)

        next_button = ttk.Button(frame,
                                 text="Next",
                                 command=lambda: self.notebook.select(self.tab2),
                                 style='TButton')
        next_button.pack(pady=20)

    def setup_player_setup_tab(self):
        frame = ttk.Frame(self.tab2, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        player1_frame = ttk.LabelFrame(frame, text="Player 1", padding="10")
        player1_frame.pack(fill=tk.X, pady=(0, 10))

        self.name1_label = ttk.Label(player1_frame,
                                     text="Enter Name:",
                                     font=("Arial", 10))
        self.name1_label.pack()

        self.name1_entry = ttk.Entry(player1_frame)
        self.name1_entry.pack(fill=tk.X, pady=(5, 0))

        self.player2_frame = ttk.LabelFrame(frame, text="Player 2", padding="10")
        self.player2_frame.pack(fill=tk.X, pady=10)

        self.name2_label = ttk.Label(self.player2_frame,
                                     text="Enter Name:",
                                     font=("Arial", 10))
        self.name2_entry = ttk.Entry(self.player2_frame)

        self.difficulty_label = ttk.Label(self.player2_frame,
                                          text="Select AI Difficulty:",
                                          font=("Arial", 10))

        self.difficulty_var = tk.IntVar(value=3)  # Default to Hard
        self.difficulty_options = [
            ("Easy", 1),
            ("Medium", 2),
            ("Hard", 3),
            ("Extreme", 4)
        ]

        self.difficulty_buttons = []
        for text, value in self.difficulty_options:
            rb = ttk.Radiobutton(self.player2_frame,
                                 text=text,
                                 variable=self.difficulty_var,
                                 value=value)
            self.difficulty_buttons.append(rb)

        button_frame = ttk.Frame(frame)
        button_frame.pack(side=tk.BOTTOM, pady=(20, 0))

        self.start_button = ttk.Button(button_frame,
                                       text="Start Game",
                                       command=self.start_game,
                                       style='TButton')
        self.start_button.pack()

        # Initialize visibility
        self.toggle_difficulty()

    def toggle_difficulty(self):
        for widget in self.player2_frame.winfo_children():
            widget.pack_forget()

        if self.option_var.get() == 1:  # Human vs AI
            self.difficulty_label.pack(pady=(0, 5))
            for rb in self.difficulty_buttons:
                rb.pack(pady=2)
        else:  # Human vs Human
            self.name2_label.pack()
            self.name2_entry.pack(fill=tk.X, pady=(5, 0))

    def start_game(self):
        board = Board()
        option = self.option_var.get()
        player_name = self.name1_entry.get()

        if option == 1:
            difficulty = self.difficulty_var.get()
            player = Player(player_name, 'X')
            computer = Computer("O", "X", difficulty)
            ui = Ui(human_player=player, board=board, computer_player=computer)
            ui.start_game_human_computer()
        elif option == 2:
            player2_name = self.name2_entry.get()
            if not player2_name:
                player2_name = "Player 2"
            player = Player(player_name, 'X')
            player2 = Player(player2_name, 'O')
            ui = Ui(human_player=player, board=board, second_player=player2)
            ui.start_game_human_human()

if __name__ == '__main__':
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()
