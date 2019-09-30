from setup import TicTacToeSetup

import random

class TicTacToe(TicTacToeSetup):

    def __init__(self):
        super(TicTacToe, self).__init__()
    
    def minimax(self, state, available_spaces, player):
        """
        Function to enable computer to pick best move
        """
        if player == self.computer:
            best = [-1, -1, -1000]
        else:
            best = [-1, -1, +1000]

        if available_spaces == 0 or self.game_over(state):
            score = self.award_score(state)
            return [-1, -1, score]

        for cell in self.empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, available_spaces - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == self.computer:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def ai_turn(self):
        """
        Function to allow a computer to play
        """
        available_spaces = len(self.empty_cells(self.board))
        if available_spaces == 0:
            return

        print(f"Computer's turn.")

        if available_spaces == 9:
            x,y = random.choice([0,1,2]), random.choice([0,1,2])
        else:
            move = self.minimax(self.board, available_spaces, self.computer)
            x, y = move[0], move[1]

        self.set_move(x, y, self.computer)
        self.print_board(self.board)


    def human_turn(self):
        """
        Function to allow a person to play
        """
        move = -1
        while move not in range(1, 10):
            try:
                move = int(input('Your turn. choose position (1..9): '))
                coord = self.valid_moves[move]
                can_move = self.set_move(coord[0], coord[1], self.human)
                self.print_board(self.board)
                if not can_move:
                    print('Bad move')
                    move = -1
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

    def start_game(self):
        """
        Function to start the game
        """
        print("Welcome to tictactoe game")
        self.print_board(self.board)
        print("You are player X \n")
        while len(self.empty_cells(self.board)) > 0 and not self.game_over(self.board):
            self.human_turn()
            self.ai_turn()

        if self.winner_found(self.board, self.human):
            print('Game over!! You win the game.')
        elif self.winner_found(self.board, self.computer):
            print('Game over!! Computer wins the game.')
        else:
            print('Game over!! DRAW.')
        exit()

game = TicTacToe()
game.start_game()
