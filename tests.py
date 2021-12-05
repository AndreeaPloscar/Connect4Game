import unittest
from board import Board
from game import Game
from player import Player
from strategy import Strategy


class Tests(unittest.TestCase):
    def setUp(self):
        self.human_player = Player(1)
        self.strategy = Strategy()
        self.computer = Player(2)
        self.board = Board(6, 7)
        self.game = Game(self.board, self.human_player, self.computer, self.strategy)

    def test_board_dimensions(self):
        self.assertEqual(self.game.get_board_dimensions(), (6, 7))

    def test_win_ai(self):
        self.board.set_value(0, 0, 2)
        self.board.set_value(0, 1, 2)
        self.board.set_value(0, 2, 2)
        self.board.set_value(1, 0, 1)
        self.board.set_value(1, 2, 1)
        self.game.computer_move()
        self.assertEqual(self.game.get_cell_value(0, 3), 2)

    def test_block_player(self):
        self.board.set_value(0, 0, 1)
        self.board.set_value(1, 0, 1)
        self.board.set_value(2, 0, 1)
        self.game.computer_move()
        self.assertEqual(self.game.get_cell_value(3, 0), 2)

    def test_block_or_win(self):
        self.board.set_value(0, 0, 1)
        self.board.set_value(1, 0, 1)
        self.board.set_value(2, 0, 1)
        self.board.set_value(0, 2, 2)
        self.board.set_value(1, 2, 2)
        self.board.set_value(2, 2, 2)
        self.game.computer_move()
        self.assertEqual(self.game.get_cell_value(3, 2), 2)
        self.assertEqual(self.game.winning_move(2), 1)

    def test_win_positive_diagonal(self):
        self.board.set_value(0, 0, 1)
        self.board.set_value(0, 1, 2)
        self.board.set_value(0, 2, 1)
        self.board.set_value(1, 2, 2)
        self.board.set_value(0, 3, 1)
        self.board.set_value(1, 3, 1)
        self.board.set_value(2, 3, 2)
        self.board.set_value(0, 4, 1)
        self.board.set_value(1, 4, 1)
        self.board.set_value(2, 4, 1)
        self.game.computer_move()
        self.assertEqual(self.game.get_cell_value(3, 4), 2)

    def test_win_negative_diagonal(self):
        self.game.human_move(0)
        self.board.set_value(1, 0, 1)
        self.board.set_value(2, 0, 1)
        self.board.set_value(3, 0, 2)
        self.board.set_value(0, 1, 1)
        self.board.set_value(1, 1, 1)
        self.board.set_value(2, 1, 2)
        self.board.set_value(0, 2, 1)
        self.board.set_value(1, 2, 2)
        self.game.computer_move()
        self.assertEqual(self.game.get_cell_value(0, 3), 2)

    def test_draw(self):
        self.board.set_value(0, 0, 1)
        self.board.set_value(0, 1, 2)
        self.board.set_value(0, 2, 1)
        self.board.set_value(0, 3, 2)
        self.board.set_value(0, 4, 1)
        self.board.set_value(0, 5, 2)
        self.board.set_value(0, 6, 1)
        self.board.set_value(1, 0, 2)
        self.board.set_value(1, 1, 1)
        self.board.set_value(1, 2, 2)
        self.board.set_value(1, 3, 1)
        self.board.set_value(1, 4, 2)
        self.board.set_value(1, 5, 1)
        self.board.set_value(1, 6, 2)
        self.board.set_value(2, 0, 2)
        self.board.set_value(2, 1, 1)
        self.board.set_value(2, 2, 2)
        self.board.set_value(2, 3, 1)
        self.board.set_value(2, 4, 2)
        self.board.set_value(2, 5, 1)
        self.board.set_value(2, 6, 2)
        self.board.set_value(3, 0, 1)
        self.board.set_value(3, 1, 2)
        self.board.set_value(3, 2, 1)
        self.board.set_value(3, 3, 2)
        self.board.set_value(3, 4, 1)
        self.board.set_value(3, 5, 2)
        self.board.set_value(3, 6, 1)
        self.board.set_value(4, 0, 1)
        self.board.set_value(4, 1, 2)
        self.board.set_value(4, 2, 1)
        self.board.set_value(4, 3, 2)
        self.board.set_value(4, 4, 1)
        self.board.set_value(4, 5, 2)
        self.board.set_value(4, 6, 1)
        self.board.set_value(5, 0, 2)
        self.board.set_value(5, 1, 1)
        self.board.set_value(5, 2, 2)
        self.board.set_value(5, 3, 1)
        self.board.set_value(5, 4, 2)
        self.board.set_value(5, 5, 1)
        self.game.computer_move()
        self.assertEqual(self.game.game_draw(), 1)

    def test_str(self):
        self.assertEqual(self.game.get_board_str(), "0 0 0 0 0 0 0\n" +
                                                    "0 0 0 0 0 0 0\n" +
                                                    "0 0 0 0 0 0 0\n" +
                                                    "0 0 0 0 0 0 0\n" +
                                                    "0 0 0 0 0 0 0\n" +
                                                    "0 0 0 0 0 0 0\n")

    def test_evaluate(self):
        self.board.set_value(0, 0, 2)
        self.board.set_value(0, 1, 2)
        self.board.set_value(0, 2, 2)
        self.game.computer_move()
        self.assertEqual(self.board.evaluate_area(self.board.get_row_values(0)), 1000000)

    def test_win_in_more_moves(self):
        pass

    def tearDown(self):
        for row in range(0, self.board.rows):
            for column in range(0, self.board.columns):
                self.board.set_value(row, column, 0)
