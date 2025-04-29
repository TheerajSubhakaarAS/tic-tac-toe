from game.board import Board
from game.player import Player

class TicTacToeCLI:
    def __init__(self):
        self.board = Board()
        self.players = [
            Player("Player 1", "X"),
            Player("Player 2", "O")
        ]
        self.current_player = 0

    def display_board(self):
        """Display the current board state."""
        print("\nCurrent Board:")
        print("-------------")
        for row in self.board.get_board():
            print("| " + " | ".join(row) + " |")
            print("-------------")

    def get_move(self) -> tuple:
        """Get move input from current player."""
        while True:
            try:
                move = input(f"\n{self.players[self.current_player].name}'s turn ({self.players[self.current_player].symbol}). Enter row and column (e.g., 1 2): ")
                row, col = map(int, move.split())
                if 1 <= row <= 3 and 1 <= col <= 3:
                    return row - 1, col - 1
                print("Invalid input. Please enter numbers between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by space.")

    def start(self):
        """Start the game loop."""
        print("Welcome to Tic Tac Toe!")
        
        while True:
            self.display_board()
            
            # Get move and make it
            row, col = self.get_move()
            if not self.board.make_move(row, col, self.players[self.current_player].symbol):
                print("Cell already occupied. Try again.")
                continue

            # Check for winner
            winner = self.board.check_winner()
            if winner:
                self.display_board()
                print(f"\nCongratulations! {self.players[self.current_player].name} wins!")
                self.players[self.current_player].increment_score()
                break

            # Check for draw
            if self.board.is_full():
                self.display_board()
                print("\nIt's a draw!")
                break

            # Switch player
            self.current_player = 1 - self.current_player

        # Display final scores
        print("\nFinal Scores:")
        for player in self.players:
            print(f"{player.name}: {player.get_score()} wins")

        # Ask to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == 'y':
            self.board.reset()
            self.current_player = 0
            self.start()
        else:
            print("\nThanks for playing!")
