#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ui.cli.cli_game import TicTacToeCLI
from ui.gui.gui_game import TicTacToeGUI

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        game = TicTacToeGUI()
    else:
        game = TicTacToeCLI()
    
    game.start()

if __name__ == "__main__":
    main()
