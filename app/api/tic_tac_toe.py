from typing import List, Optional
from pydantic import BaseModel
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from game.board import Board
from game.player import Player

class Cell(BaseModel):
    row: int
    col: int
    value: str

class GameState(BaseModel):
    board: List[List[Cell]]
    current_player: str
    winner: Optional[str] = None
    game_over: bool
    score: dict

class Move(BaseModel):
    row: int
    col: int
    player: str

# Game state storage
games = {}

# Global players list to maintain scores
players = [
    Player("Player 1", "X"),
    Player("Player 2", "O")
]

def new_game() -> GameState:
    """Create a new game."""
    game_id = len(games) + 1
    board = Board()
    current_player = 0
    
    games[game_id] = {
        "board": board,
        "current_player": current_player
    }
    
    return GameState(
        board=[[Cell(row=r, col=c, value=board.board[r][c]) 
               for c in range(3)] for r in range(3)],
        current_player=players[current_player].symbol,
        winner=None,
        game_over=False,
        score={player.name: player.score for player in players}
    )

def make_move(move: Move) -> GameState:
    """Make a move in the game."""
    game_id = len(games)
    game = games.get(game_id)
    
    if not game:
        return new_game()
    
    board = game["board"]
    current_player = game["current_player"]
    winner = None
    game_over = False
    
    if players[current_player].symbol != move.player:
        return GameState(
            board=[[Cell(row=r, col=c, value=board.board[r][c]) 
                   for c in range(3)] for r in range(3)],
            current_player=players[current_player].symbol,
            winner=None,
            game_over=False,
            score={player.name: player.score for player in players}
        )
    
    if board.make_move(move.row, move.col, move.player):
        winner = board.check_winner()
        if winner:
            game_over = True
            players[current_player].increment_score()
        elif board.is_full():
            game_over = True
        else:
            current_player = 1 - current_player
            game["current_player"] = current_player
    
    # Return the current game state with win information
    return GameState(
        board=[[Cell(row=r, col=c, value=board.board[r][c]) 
               for c in range(3)] for r in range(3)],
        current_player=players[current_player].symbol,
        winner=winner if winner else None,
        game_over=game_over,
        score={player.name: player.score for player in players}
    )

def new_game() -> GameState:
    """Create a new game."""
    game_id = len(games) + 1
    board = Board()
    current_player = 0
    
    games[game_id] = {
        "board": board,
        "current_player": current_player
    }
    
    return GameState(
        board=[[Cell(row=r, col=c, value=board.board[r][c]) 
               for c in range(3)] for r in range(3)],
        current_player=players[current_player].symbol,
        winner=None,
        game_over=False,
        score={player.name: player.score for player in players}
    )
