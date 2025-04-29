import tkinter as tk
from tkinter import messagebox
from game.board import Board
from game.player import Player

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x350")
        
        self.board = Board()
        self.players = [
            Player("Player 1", "X"),
            Player("Player 2", "O")
        ]
        self.current_player = 0
        
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        """Create all GUI widgets."""
        # Create buttons for the board
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        # Create status label
        self.status_label = tk.Label(
            self.window,
            text=f"{self.players[self.current_player].name}'s turn",
            font=('Arial', 12)
        )
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Create reset button
        reset_button = tk.Button(
            self.window,
            text="Reset",
            font=('Arial', 12),
            command=self.reset_game
        )
        reset_button.grid(row=4, column=0, columnspan=3, pady=10)

    def make_move(self, row: int, col: int):
        """Handle button click and make move."""
        if self.board.make_move(row, col, self.players[self.current_player].symbol):
            self.buttons[row][col].config(text=self.players[self.current_player].symbol, state='disabled')
            
            # Check for winner
            winner = self.board.check_winner()
            if winner:
                self.buttons[row][col].config(text=self.players[self.current_player].symbol)
                self.players[self.current_player].increment_score()
                self.show_winner()
                return

            # Check for draw
            if self.board.is_full():
                self.show_draw()
                return

            # Switch player
            self.current_player = 1 - self.current_player
            self.status_label.config(text=f"{self.players[self.current_player].name}'s turn")

    def show_winner(self):
        """Show winner message and update scores."""
        messagebox.showinfo(
            "Game Over",
            f"{self.players[self.current_player].name} wins!\n\n" +
            f"Scores:\nPlayer 1: {self.players[0].get_score()}\n" +
            f"Player 2: {self.players[1].get_score()}"
        )
        self.reset_game()

    def show_draw(self):
        """Show draw message."""
        messagebox.showinfo(
            "Game Over",
            "It's a draw!\n\n" +
            f"Scores:\nPlayer 1: {self.players[0].get_score()}\n" +
            f"Player 2: {self.players[1].get_score()}"
        )
        self.reset_game()

    def reset_game(self):
        """Reset the game to initial state."""
        self.board.reset()
        self.current_player = 0
        self.status_label.config(text=f"{self.players[self.current_player].name}'s turn")
        
        # Reset all buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state='normal')

    def start(self):
        """Start the GUI application."""
        self.window.mainloop()
