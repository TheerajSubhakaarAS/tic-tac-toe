class Board:
    def __init__(self):
        self.size = 3
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.empty_cells = self.size * self.size
        self.first_move_after_win = False

    def make_move(self, row: int, col: int, player: str) -> bool:
        """
        Make a move on the board.
        Returns True if move was successful, False otherwise.
        """
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            self.empty_cells -= 1
            if self.first_move_after_win:
                self.first_move_after_win = False
            return True
        return False

    def check_winner(self) -> str:
        """
        Check if there's a winner.
        Returns 'X', 'O', or '' if no winner.
        """
        # Check rows and columns
        for i in range(self.size):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return ''

    def is_full(self) -> bool:
        """Check if the board is full."""
        return self.empty_cells == 0

    def is_first_move(self) -> bool:
        """Check if this is the first move after a win."""
        return self.first_move_after_win

    def reset(self):
        """Reset the board to initial state."""
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.empty_cells = self.size * self.size
        self.first_move_after_win = True

    def get_board(self) -> list:
        """Return the current board state."""
        return self.board
