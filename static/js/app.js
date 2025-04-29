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
        });
    }

    // Update the board display
    function updateBoard() {
        cells.forEach(cell => {
            const row = parseInt(cell.dataset.row);
            const col = parseInt(cell.dataset.col);
            const cellData = currentGame.board[row][col];
            cell.textContent = cellData.value === ' ' ? '' : cellData.value;
            cell.classList.toggle('disabled', currentGame.game_over || cellData.value !== ' ');
        });
    }

    // Update scores display
    function updateScores() {
        player1Score.textContent = currentGame.score['Player 1'];
        player2Score.textContent = currentGame.score['Player 2'];
    }

    // Check game status and update UI
    function checkGameStatus() {
        if (currentGame.game_over) {
            if (currentGame.winner) {
                gameStatus.textContent = `${currentGame.winner} wins!`;
                gameStatus.classList.add('winner');
            } else {
                gameStatus.textContent = 'It\'s a draw!';
                gameStatus.classList.add('draw');
            }
        } else {
            currentPlayer.textContent = `Player ${currentGame.current_player === 'X' ? '1' : '2'}'s turn (${currentGame.current_player})`;
            gameStatus.textContent = '';
            gameStatus.classList.remove('winner', 'draw');
        }
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
