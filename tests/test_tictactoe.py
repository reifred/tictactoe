from app.setup import TicTacToeSetup

import unittest

class TestTicTacToe(unittest.TestCase):

    def test_empty_cells(self):
        ticTacToeSetup = TicTacToeSetup()
        board = [[0, 0, 0], [0, 0, 0], [1, -1, 1]]
        cells = ticTacToeSetup.empty_cells(board)
        self.assertEqual(len(cells), 6)

    def test_can_set_move_on_empty_cell(self):
        ticTacToeSetup = TicTacToeSetup()
        ticTacToeSetup.board = [[0, 0, 0], [0, 0, 0], [1, -1, 1]]
        self.assertEqual(ticTacToeSetup.board[0][0], 0)
        result = ticTacToeSetup.set_move(0, 0, 1)
        self.assertEqual(result, True)
        self.assertEqual(ticTacToeSetup.board[0][0], 1)

    def test_cannot_set_move_on_filled_cell(self):
        ticTacToeSetup = TicTacToeSetup()
        ticTacToeSetup.board = [[0, 0, 0], [0, 0, 0], [1, -1, 1]]
        result = ticTacToeSetup.set_move(2, 2, 1)
        self.assertEqual(result, False)

    def test_winner_found_if_some_cells_have_same_player_number(self):
        ticTacToeSetup = TicTacToeSetup()
        ticTacToeSetup.board = [[0, 0, 0], [1, 1, 1], [1, -1, 1]]
        result = ticTacToeSetup.winner_found(ticTacToeSetup.board, 1)
        self.assertEqual(result, True)

    def test_winner_not_found_if_cells_have_no_same_player_number(self):
        ticTacToeSetup = TicTacToeSetup()
        ticTacToeSetup.board = [[0, 0, 0], [1, 0, 1], [1, -1, 1]]
        result = ticTacToeSetup.winner_found(ticTacToeSetup.board, 1)
        self.assertEqual(result, False)

    def test_score_should_be_one_if_computer_has_won(self):
        ticTacToeSetup = TicTacToeSetup()
        ticTacToeSetup.board = [[0, 0, 0], [1, 1, 1], [1, -1, 1]]
        score = ticTacToeSetup.award_score(ticTacToeSetup.board)
        self.assertEqual(score, 1)

    def test_score_should_be_negative_one_if_human_has_won(self):
        ticTacToeSetup = TicTacToeSetup()
        ticTacToeSetup.board = [[0, 0, 0], [-1,- 1, -1], [1, -1, 1]]
        score = ticTacToeSetup.award_score(ticTacToeSetup.board)
        self.assertEqual(score, -1)

    def test_score_should_be_zero_if_the_game_is_a_tie(self):
        ticTacToeSetup = TicTacToeSetup()
        ticTacToeSetup.board = [[0, 0, 0], [-1, 0, -1], [1, -1, 1]]
        score = ticTacToeSetup.award_score(ticTacToeSetup.board)
        self.assertEqual(score, 0)

    def test_game_over_if_winner_found(self):
        ticTacToeSetup = TicTacToeSetup()
        is_game_over = ticTacToeSetup.game_over(ticTacToeSetup.board)
        self.assertEqual(is_game_over, False)
        ticTacToeSetup.board = [[0, 0, 0], [-1, -1, -1], [1, -1, 1]]
        ticTacToeSetup.award_score(ticTacToeSetup.board)
        is_game_over = ticTacToeSetup.game_over(ticTacToeSetup.board)
        self.assertEqual(is_game_over, True)

if __name__ == '__main__':
    unittest.main()
