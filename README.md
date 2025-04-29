# Tic Tac Toe Game

A classic Tic Tac Toe game implementation using Python. This project provides both a command-line interface (CLI) and a graphical user interface (GUI) version of the game.

## Tech Stack

- **Programming Language**: Python 3.8+
- **GUI Framework**: Tkinter (for GUI version)
- **Core Technologies**:
  - Object-Oriented Programming
  - Game Logic Implementation
  - User Interface Design
  - Event Handling

## Project Structure

```
tic-tac-toe/
├── src/                     # Source code directory
│   ├── game/               # Game logic implementation
│   │   ├── board.py        # Game board implementation
│   │   ├── player.py       # Player class implementation
│   │   └── game.py         # Main game logic
│   ├── ui/                 # User interface implementations
│   │   ├── cli/           # Command Line Interface
│   │   │   └── cli_game.py
│   │   └── gui/           # Graphical User Interface
│   │       └── gui_game.py
│   └── main.py             # Entry point of the application
├── tests/                  # Test files
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Features

- Two-player game mode
- Command-line and GUI interfaces
- Valid move checking
- Win condition checking
- Score tracking
- Game reset functionality

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python src/main.py
   ```

## Contributing

Feel free to submit issues and enhancement requests!
