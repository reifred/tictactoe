class TicTacToeSetup(object):

    def __init__(self):
        self.human = -1
        self.computer = +1
        self.draw = 0
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.valid_moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

    def empty_cells(self, current_board):
        """
        Function to return a list of empty cells
        """
        cells = []

        for x, row in enumerate(current_board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def print_board(self, current_board):
        """
        Function to print the current state of the board
        """
        pieces = { self.human: 'X', self.computer: 'O', self.draw: ' '}

        print('---------------')
        for row in current_board:
            for cell in row:
                print(f'| {pieces[cell]} ', end='|')
            print('\n', '---------------')

    def set_move(self, x, y, player):
        """
        Function to determine if a player can play in a particular cell
        """
        if [x, y] in self.empty_cells(self.board):
            self.board[x][y] = player
            return True
        return False

    def winner_found(self, current_board, player):
        """
        Function to determine if a winner has been found depending on the current board
        """
        winning_state = [
            [current_board[0][0], current_board[0][1], current_board[0][2]],
            [current_board[1][0], current_board[1][1], current_board[1][2]],
            [current_board[2][0], current_board[2][1], current_board[2][2]],
            [current_board[0][0], current_board[1][0], current_board[2][0]],
            [current_board[0][1], current_board[1][1], current_board[2][1]],
            [current_board[0][2], current_board[1][2], current_board[2][2]],
            [current_board[0][0], current_board[1][1], current_board[2][2]],
            [current_board[2][0], current_board[1][1], current_board[0][2]],
        ]
        if [player, player, player] in winning_state:
            return True
        return False

    def award_score(self, current_board):
        """
        Function to award score based on computer win, human win or tie
        """
        if self.winner_found(current_board, self.computer):
            score = +1
        elif self.winner_found(current_board, self.human):
            score = -1
        else:
            score = 0

        return score

    def game_over(self, current_board):
        """
        Function to end the game incase of a player's win
        """
        return self.winner_found(current_board, self.human) or self.winner_found(current_board, self.computer)
