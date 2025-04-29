# Tic Tac Toe Game

A classic Tic Tac Toe game implementation using Python. This project provides three versions of the game:
1. Command-line interface (CLI)
2. Graphical user interface (GUI)
3. Web-based interface using FastAPI

## Tech Stack

- **Backend**: Python 3.8+
- **Web Framework**: FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Core Technologies**:
  - Object-Oriented Programming
  - RESTful API Design
  - WebSocket Support (planned)
  - Responsive Web Design

## Project Structure

```
tic-tac-toe/
├── app/                      # FastAPI application
│   ├── api/                 # API endpoints
│   │   └── tic_tac_toe.py   # Game API implementation
│   ├── templates/           # HTML templates
│   │   └── index.html       # Main game page
│   └── main.py              # FastAPI application entry point
├── static/                  # Static files
│   ├── css/                # Stylesheets
│   │   └── style.css       # Main stylesheet
│   └── js/                 # JavaScript files
│       └── app.js          # Game logic
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
- Three interface options:
  - Command-line interface
  - Desktop GUI
  - Web-based interface
- Valid move checking
- Win condition checking
- Score tracking
- Game reset functionality
- Responsive web design

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd tic-tac-toe
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install tkinter (for GUI version):
   ```bash
   sudo apt-get install python3-tk
   ```

## Usage

### Command Line Version

Run the CLI version:
```bash
python src/main.py
```

### GUI Version

Run the GUI version:
```bash
python src/main.py --gui
```

### Web Version

1. Navigate to the project directory:
   ```bash
   cd tic-tac-toe
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Start the FastAPI server:
   ```bash
   python app/main.py
   ```
   The server will start on http://0.0.0.0:8000

4. Open your web browser and navigate to:
   ```
   http://localhost:8000
   ```

5. Use the web interface to play the game

   To stop the server, press `Ctrl+C` in the terminal.

## API Endpoints

- `GET /api/game/new`: Create a new game
- `POST /api/game/move`: Make a move in the game
- `GET /`: Serve the web interface

## Contributing

Feel free to submit issues and enhancement requests!
