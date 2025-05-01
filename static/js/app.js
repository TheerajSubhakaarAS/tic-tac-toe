document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell');
    const newGameBtn = document.getElementById('new-game');
    const currentPlayer = document.getElementById('current-player');
    const gameStatus = document.getElementById('game-status');
    const player1Score = document.getElementById('player1-score');
    const player2Score = document.getElementById('player2-score');

    let currentGame = null;

    // Initialize new game
    function newGame() {
        fetch('/api/game/new')
            .then(response => response.json())
            .then(data => {
                currentGame = data;
                updateBoard();
                updateScores();
                checkGameStatus();
                
                // Clear the game status
                gameStatus.textContent = '';
                gameStatus.classList.remove('winner', 'draw');
                currentPlayer.textContent = `Player ${currentGame.current_player === 'X' ? '1' : '2'}'s turn (${currentGame.current_player})`;
            });
    }

    // Make a move
    function makeMove(row, col) {
        const move = {
            row: row,
            col: col,
            player: currentGame.current_player
        };

        fetch('/api/game/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(move)
        })
        .then(response => response.json())
        .then(data => {
            currentGame = data;
            updateBoard();
            updateScores();
            checkGameStatus();
            
            // If game is over, prepare for next game
            if (currentGame.game_over) {
                currentPlayer.textContent = `Player ${currentGame.current_player === 'X' ? '1' : '2'}'s turn (${currentGame.current_player})`;
                
                // Add celebration effects
                if (currentGame.winner) {
                    addWinningLine();
                    addConfetti();
                    
                    // Remove celebration effects after 3 seconds and start new game
                    setTimeout(() => {
                        removeWinningLine();
                        removeConfetti();
                        fetch('/api/game/new')
                            .then(response => response.json())
                            .then(data => {
                                currentGame = data;
                                updateBoard();
                                updateScores();
                                checkGameStatus();
                                
                                // Clear the game status
                                gameStatus.textContent = '';
                                gameStatus.classList.remove('winner', 'draw');
                                currentPlayer.textContent = `Player ${currentGame.current_player === 'X' ? '1' : '2'}'s turn (${currentGame.current_player})`;
                            });
                    }, 3000);
                }
            }
        });
    }

    // Update the board display
    function updateBoard() {
        cells.forEach(cell => {
            const row = parseInt(cell.dataset.row);
            const col = parseInt(cell.dataset.col);
            const cellData = currentGame.board[row][col];
            cell.textContent = cellData.value === ' ' ? '' : cellData.value;
            cell.classList.remove('disabled', 'winner-cell');
            
            // Add winner cell animation if this cell was part of the winning combination
            if (currentGame.winner && currentGame.winner === cell.textContent) {
                cell.classList.add('winner-cell');
            }
        });
    }

    // Update scores display
    function updateScores() {
        player1Score.textContent = currentGame.score['Player 1'];
        player2Score.textContent = currentGame.score['Player 2'];
    }

    // Check game status and update UI
    function checkGameStatus() {
        if (currentGame.winner) {
            gameStatus.textContent = `${currentGame.winner} wins!`;
            gameStatus.classList.add('winner');
        } else if (currentGame.game_over) {
            gameStatus.textContent = 'It\'s a draw!';
            gameStatus.classList.add('draw');
        } else {
            currentPlayer.textContent = `Player ${currentGame.current_player === 'X' ? '1' : '2'}'s turn (${currentGame.current_player})`;
            gameStatus.textContent = '';
            gameStatus.classList.remove('winner', 'draw');
        }
    }

    // Add winning line animation
    function addWinningLine() {
        const winningLine = document.createElement('div');
        winningLine.className = 'winning-line';
        document.body.appendChild(winningLine);
        
        // Position the line based on the winning combination
        const winningCombination = getWinningCombination();
        if (winningCombination) {
            const firstCell = document.querySelector(`[data-row="${winningCombination[0].row}"][data-col="${winningCombination[0].col}"]`);
            const lastCell = document.querySelector(`[data-row="${winningCombination[winningCombination.length - 1].row}"][data-col="${winningCombination[winningCombination.length - 1].col}"]`);
            
            if (firstCell && lastCell) {
                const rect = firstCell.getBoundingClientRect();
                winningLine.style.left = `${rect.left}px`;
                winningLine.style.top = `${rect.top + rect.height / 2}px`;
                
                const lastRect = lastCell.getBoundingClientRect();
                winningLine.style.width = `${lastRect.left + lastRect.width - rect.left}px`;
            }
        }
    }

    // Remove winning line
    function removeWinningLine() {
        const winningLine = document.querySelector('.winning-line');
        if (winningLine) {
            winningLine.remove();
        }
    }

    // Add confetti effect
    function addConfetti() {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        document.body.appendChild(confetti);
        
        // Create multiple confetti pieces
        for (let i = 0; i < 50; i++) {
            const piece = document.createElement('div');
            piece.className = 'confetti-piece';
            piece.style.left = `${Math.random() * 100}%`;
            piece.style.animationDelay = `${Math.random()}s`;
            confetti.appendChild(piece);
        }
    }

    // Remove confetti
    function removeConfetti() {
        const confetti = document.querySelector('.confetti');
        if (confetti) {
            confetti.remove();
        }
    }

    // Get winning combination cells
    function getWinningCombination() {
        const board = currentGame.board;
        const winningCombination = [];
        
        // Check rows
        for (let i = 0; i < 3; i++) {
            if (board[i][0].value === board[i][1].value && board[i][1].value === board[i][2].value && board[i][0].value !== ' ') {
                winningCombination.push({row: i, col: 0}, {row: i, col: 1}, {row: i, col: 2});
                return winningCombination;
            }
        }
        
        // Check columns
        for (let i = 0; i < 3; i++) {
            if (board[0][i].value === board[1][i].value && board[1][i].value === board[2][i].value && board[0][i].value !== ' ') {
                winningCombination.push({row: 0, col: i}, {row: 1, col: i}, {row: 2, col: i});
                return winningCombination;
            }
        }
        
        // Check diagonals
        if (board[0][0].value === board[1][1].value && board[1][1].value === board[2][2].value && board[0][0].value !== ' ') {
            winningCombination.push({row: 0, col: 0}, {row: 1, col: 1}, {row: 2, col: 2});
            return winningCombination;
        }
        
        if (board[0][2].value === board[1][1].value && board[1][1].value === board[2][0].value && board[0][2].value !== ' ') {
            winningCombination.push({row: 0, col: 2}, {row: 1, col: 1}, {row: 2, col: 0});
            return winningCombination;
        }
        
        return null;
    }

    // Event listeners
    cells.forEach(cell => {
        cell.addEventListener('click', () => {
            if (currentGame.game_over || cell.textContent !== '') return;
            
            const row = parseInt(cell.dataset.row);
            const col = parseInt(cell.dataset.col);
            makeMove(row, col);
        });
    });

    newGameBtn.addEventListener('click', newGame);

    // Start new game on page load
    newGame();
});
